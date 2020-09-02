from tf_explain.core import GradientsInputs as tf_explain_GradientsInputs

from xplainer.backend.tools.abstract_tf_explain_basic import AbstractTfExplainBasicTool


class GradientsInputs(AbstractTfExplainBasicTool):
    def __init__(self):
        super().__init__(tf_explain_GradientsInputs)

    def name(self):
        return "Gradients Inputs"

    def category(self):
        return "Gradient Based"
