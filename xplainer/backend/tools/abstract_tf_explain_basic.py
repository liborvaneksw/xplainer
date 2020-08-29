from abc import ABC

from xplainer.backend.tools import AbstractTool
from xplainer.backend.utils.image import prepare_for_prediction, get_base64png


class AbstractTfExplainBasicTool(AbstractTool, ABC):
    """
    Implementation of common methods for tf-explain tools.
    """

    def __init__(self, explain_class):
        self.explain_class = explain_class

    def source_name(self) -> str:
        return "tf-explain"

    def source_url(self) -> str:
        return "https://github.com/sicara/tf-explain"

    def explain_one(self, model, image_path, label, tool_settings):
        image = prepare_for_prediction(model, image_path)
        result_image = self.explain_class().explain((image.numpy(), None), model, class_index=label, **tool_settings)
        image_base46 = get_base64png(result_image)

        return image_base46
