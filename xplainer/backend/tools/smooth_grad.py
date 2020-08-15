from tf_explain.core import SmoothGrad as tf_explain_SmoothGrad

from xplainer.backend.tools.abstract_tf_explain_basic import AbstractTfExplainBasicTool


class SmoothGrad(AbstractTfExplainBasicTool):
    def name(self):
        return "SmoothGrad"

    def category(self):
        return "Gradient Based"

    def explain(self, model, image_path):
        return super()._explain(model, image_path, tf_explain_SmoothGrad)
