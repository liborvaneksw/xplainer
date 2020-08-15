from tf_explain.core import GradientsInputs as tf_explain_GradientsInputs

from xplainer.backend.tools.abstract_tf_explain_basic import AbstractTfExplainBasicTool


class GradientsInputs(AbstractTfExplainBasicTool):
    def name(self):
        return "GradientsInputs"

    def category(self):
        return "Gradient Based"

    def explain(self, model, image_path):
        return super()._explain(model, image_path, tf_explain_GradientsInputs)
