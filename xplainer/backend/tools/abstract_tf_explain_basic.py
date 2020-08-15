from abc import ABC

import tensorflow as tf

from xplainer.backend.tools import AbstractTool
from xplainer.backend.utils.image import prepare_for_prediction, get_base64png


class AbstractTfExplainBasicTool(AbstractTool, ABC):
    """
    Implementation of common methods for tf-explain tools.
    """

    def source_name(self) -> str:
        return "tf-explain"

    def source_url(self) -> str:
        return "https://github.com/sicara/tf-explain"

    def _explain(self, model, image_path, explain_class):
        image = prepare_for_prediction(model, image_path)

        label_onehot = model.predict(image)[0]
        label = tf.math.argmax(label_onehot)
        result_image = explain_class().explain((image.numpy(), None), model, class_index=label.numpy())

        image_base46 = get_base64png(result_image)

        result = {"label_id": int(label), "image": image_base46}

        return result
