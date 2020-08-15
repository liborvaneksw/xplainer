from tf_explain.core import IntegratedGradients as tf_explain_IntegratedGradients

from xplainer.backend.tools.abstract_tf_explain_basic import AbstractTfExplainBasicTool


class IntegratedGradients(AbstractTfExplainBasicTool):
    def name(self):
        return "IntegratedGradients"

    def category(self):
        return "Gradient Based"

    def explain(self, model, image_path):
        return super()._explain(model, image_path, tf_explain_IntegratedGradients)
