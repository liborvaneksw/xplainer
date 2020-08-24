from tf_explain.core import SmoothGrad as tf_explain_SmoothGrad

from xplainer.backend.tools.abstract_tf_explain_basic import AbstractTfExplainBasicTool


class SmoothGrad(AbstractTfExplainBasicTool):
    def __init__(self):
        super().__init__(tf_explain_SmoothGrad)

    def name(self):
        return "SmoothGrad"

    def category(self):
        return "Gradient Based"
