import tensorflow as tf
from lime import lime_image
from skimage.segmentation import mark_boundaries

from xplainer.backend.tools.abstract_tool import AbstractTool, GeneralSettings
from xplainer.backend.utils.image import prepare_for_prediction, get_base64png


class Lime(AbstractTool):
    def name(self):
        return "LIME"

    def category(self):
        return "Local"

    def description(self):
        return "Local Interpretable Model-Agnostic Explanations."

    def source_name(self) -> str:
        return "lime"

    def source_url(self) -> str:
        return "https://github.com/marcotcr/lime"

    def tool_parameters(self) -> dict:
        return {
            "list": [
                {
                    "param": "batch_size",
                    "name": "Batch size",
                    "type": "int",
                    "default": 10,
                    "min": 1,
                    "step": 1,
                },
                {
                    "param": "num_features",
                    "name": "Features",
                    "type": "int",
                    "default": 100000,
                    "min": 1,
                    "step": 10000,
                },
                {
                    "param": "num_samples",
                    "name": "Samples",
                    "type": "int",
                    "default": 100,
                    "min": 1,
                    "step": 100,
                },
                {
                    "param": "positive_only",
                    "name": "Positive only",
                    "type": "bool",
                    "default": True,
                },
                {
                    "param": "superpixels",
                    "name": "Superpixels",
                    "type": "int",
                    "default": 5,
                    "min": 1,
                    "step": 1,
                },
                {
                    "param": "min_weight",
                    "name": "Min weight",
                    "type": "float",
                    "default": 0.0,
                    "min": 0.0,
                    "step": 0.1,
                },
                {"param": "hide_rest", "name": "Hide rest", "description": None, "type": "bool", "default": True,},
            ],
            "layout": [
                ["batch_size", "num_features", "num_samples"],
                ["superpixels", "min_weight", "positive_only", "hide_rest"],
            ],
        }

    def explain(
        self, model: tf.keras.Model, image_path: str, general_settings: GeneralSettings, tool_settings: dict = None
    ) -> list:
        image = prepare_for_prediction(model, image_path)
        onehot, labels = self._get_labels(model, image, general_settings)

        image = tf.cast(image, dtype=tf.float64)
        explainer = lime_image.LimeImageExplainer()
        explanation = explainer.explain_instance(
            image.numpy()[0],
            model.predict,
            labels=labels,
            batch_size=tool_settings["batch_size"],
            num_features=tool_settings["num_features"],
            num_samples=tool_settings["num_samples"],
        )

        results = []
        for label in labels:
            temp, mask = explanation.get_image_and_mask(
                label,
                positive_only=tool_settings["positive_only"],
                num_features=tool_settings["superpixels"],
                min_weight=tool_settings["min_weight"],
                hide_rest=tool_settings["hide_rest"],
            )

            result_image = mark_boundaries(temp / 2 + 0.5, mask)
            result_image = tf.image.convert_image_dtype(result_image, dtype=tf.uint8, saturate=True)

            image_base46 = get_base64png(result_image)
            results.append(
                {"label_id": int(label), "probability": float(onehot[label]), "image": image_base46,}
            )

        return results
