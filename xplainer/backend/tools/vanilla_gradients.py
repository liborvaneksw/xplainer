from tf_explain.core import VanillaGradients as tf_explain_VanillaGradients

from xplainer.backend.tools.abstract_tf_explain_basic import AbstractTfExplainBasicTool


class VanillaGradients(AbstractTfExplainBasicTool):
    def name(self):
        return "Vanilla Gradient"

    def category(self):
        return "Gradient Based"

    def explain(self, model, image_path):
        return super()._explain(model, image_path, tf_explain_VanillaGradients)
