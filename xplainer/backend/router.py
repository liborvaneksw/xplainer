import base64
import json
import os
import uuid

import cv2
import tensorflow as tf
from flask import request, session, make_response
from flask import send_file, send_from_directory, jsonify, Flask, Response

from xplainer.backend.toolkit import ToolKit
from xplainer.backend.tools.abstract_tool import GeneralSetup
from xplainer.backend.utils.image import get_base64png, prepare_for_prediction, create_thumbnail
from xplainer.backend.utils.model import get_params_count, get_input_shape, is_flat


def register_routes(app: Flask, tmp_dir: str, model: tf.keras.Model, frontend: bool) -> None:
    toolbox = ToolKit()

    @app.route("/api/model", methods=["GET"])
    def model_info():
        parameters = get_params_count(model)
        flat = is_flat(model)
        input_shape = get_input_shape(model)
        info = {
            "path": app.config["model"],
            "parameters": int(parameters),
            "is_flat": bool(flat),
            "input_shape": tuple(int(s) for s in input_shape),
        }
        return jsonify(info)

    @app.route("/api/model/plot", methods=["GET"])
    def model_plot():
        return send_file(os.path.join(tmp_dir, "model_plot.png"), mimetype="image/png")

    @app.route("/api/model/summary", methods=["GET"])
    def model_summary():
        stringlist = []
        model.summary(print_fn=lambda x: stringlist.append(x))
        short_model_summary = "\n".join(stringlist)
        return Response(short_model_summary, mimetype="text")

    @app.route("/api/tools", methods=["GET"])
    def tools():
        by_category = request.args.get("by_category")
        return jsonify(toolbox.get_tools(by_category))

    @app.route("/api/tools/categories", methods=["GET"])
    def categories():
        return jsonify(toolbox.get_categories())

    @app.route("/api/tools/<string:name>", methods=["GET"])
    def tool_detail(name: str):
        tool = toolbox.get_tool(name)
        if tool is None:
            return make_response(jsonify({"error": f"Invalid tool id '{name}'."}), 404)

        return jsonify(tool.to_json(detail=True))

    @app.route("/api/tools/<string:name>/explain", methods=["POST"])
    def tool_explain(name: str):
        tool = toolbox.get_tool(name)
        general_setup = request.json["general_setup"]
        if tool is None:
            return make_response(jsonify({"error": f"Invalid tool id '{name}'."}), 404)

        try:
            general_setup = GeneralSetup(general_setup)
        except (KeyError, ValueError) as e:
            return make_response(jsonify({"error": f"General setup is invalid."}), 400)

        image_path = os.path.join(tmp_dir, session["image_id"] + ".png")
        result = tool.explain(model, image_path, general_setup)
        return json.dumps(result)

    @app.route("/api/image", methods=["PUT"])
    def image_upload():
        name = request.json["name"]
        data = request.json["base64"]
        image = base64.b64decode(data)

        image_identifier = str(uuid.uuid4())
        session["image_name"] = name
        session["image_id"] = image_identifier

        with open(os.path.join(tmp_dir, image_identifier + ".png"), "wb") as file:
            file.write(image)

        image_thumbnail = create_thumbnail(image, 100)
        cv2.imwrite(os.path.join(tmp_dir, image_identifier + "_thumbnail.png"), image_thumbnail)

        return make_response(jsonify({"name": name}), 200)

    @app.route("/api/image", methods=["GET"])
    def image_download():
        image_path = os.path.join(tmp_dir, session["image_id"] + ".png")
        return get_base64png(image_path)

    @app.route("/api/image/thumbnail", methods=["GET"])
    def image_thumbnail_download():
        image_path = os.path.join(tmp_dir, session["image_id"] + "_thumbnail.png")
        return get_base64png(image_path)

    @app.route("/api/image/predict", methods=["GET"])
    def image_predict():
        image_path = os.path.join(tmp_dir, session["image_id"] + ".png")
        image = prepare_for_prediction(model, image_path)

        label_onehot = model.predict(image)[0]
        result = [float(x) for x in list(label_onehot)]
        return jsonify(result)

    #
    # frontend follows
    #

    if not frontend:
        return

    # path to the build frontend
    dist_path = os.path.join(os.path.dirname(__file__), "../webapp/dist/webapp/")

    @app.route("/<path:path>")
    def static_proxy(path: str):
        """
        Serves static files and the root, if the user starts the app on a non-root URL.

        It was not easy to determine this precisely, therefore we use proxy - if the file is a static source, serve it.
        If not, try to serve root.
        """
        if os.path.exists(os.path.join(dist_path, path)):
            return send_from_directory(dist_path, path)
        else:
            return root()

    @app.route("/")
    def root():
        return send_from_directory(dist_path, "index.html")
