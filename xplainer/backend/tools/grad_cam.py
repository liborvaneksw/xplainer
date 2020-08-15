from tf_explain.core import GradCAM as tf_explain_GradCam

from xplainer.backend.tools.abstract_tf_explain_basic import AbstractTfExplainBasicTool


class GradCam(AbstractTfExplainBasicTool):
    def name(self):
        return "GradCam"

    def category(self):
        return "Gradient Based"

    def explain(self, model, image_path):
        return super()._explain(model, image_path, tf_explain_GradCam)
