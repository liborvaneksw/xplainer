from tf_explain.core import GradCAM as tf_explain_GradCam

from xplainer.backend.tools.abstract_tf_explain_basic import AbstractTfExplainBasicTool


class GradCam(AbstractTfExplainBasicTool):
    def __init__(self):
        super().__init__(tf_explain_GradCam)

    def name(self):
        return "GradCam"

    def category(self):
        return "Gradient Based"
