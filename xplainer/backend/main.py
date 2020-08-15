import argparse
import tempfile

from flask import Flask
from flask_cors import CORS

from xplainer.backend.router import register_routes
from xplainer.backend.utils.model import load_and_analyze


def create_and_run_app(debug=False):
    parser = argparse.ArgumentParser(description="xxx")
    parser.add_argument("--model", type=str, help="your model file")
    # parser.add_argument("--port", type=int, default=5005, help="port for running the backend")
    args = parser.parse_args()

    with tempfile.TemporaryDirectory() as tmp_dir:
        app = create_app(args, tmp_dir=tmp_dir, debug=debug)
        app.run(host="127.0.0.1", port=5005)


def create_app(args, tmp_dir, debug=False):
    app = Flask(__name__)
    CORS(app, supports_credentials=True)
    app.secret_key = "~`_Dg@qr+NJ?9~LkuB'*Q2_q,A]_ay<"  # needed for session
    app.config["model"] = args.model

    print("----------------------------------------------------------")
    print("Loading and analyzing model. This might take a while.")
    print("----------------------------------------------------------")

    model = load_and_analyze(args.model, tmp_dir)

    print("----------------------------------------------------------")
    print("Loading done. Application is stating.")
    print("----------------------------------------------------------")

    register_routes(app, tmp_dir, model, not debug)

    return app


if __name__ == "__main__":
    create_and_run_app(debug=True)
