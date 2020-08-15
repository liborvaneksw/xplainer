import tensorflow as tf
from lime import lime_image
from skimage.segmentation import mark_boundaries

from xplainer.backend.tools.abstract_tool import AbstractTool
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

    def explain(self, model, image_path):
        image = prepare_for_prediction(model, image_path, expand_dims=False)

        label_onehot = model.predict(tf.expand_dims(image, 0))[0]
        label = tf.math.argmax(label_onehot)

        image = tf.cast(image, dtype=tf.float64)
        explainer = lime_image.LimeImageExplainer()
        explanation = explainer.explain_instance(image.numpy(), model.predict, top_labels=5, hide_color=0, num_samples=500)
        temp, mask = explanation.get_image_and_mask(label.numpy(), positive_only=True, num_features=5, hide_rest=True)

        result_image = mark_boundaries(temp / 2 + 0.5, mask)
        result_image = tf.image.convert_image_dtype(result_image, dtype=tf.uint8, saturate=True)

        image_base46 = get_base64png(result_image)
        result = {"label_id": float(label), "image": image_base46}
        return result
