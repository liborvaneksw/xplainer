from tf_explain.core import IntegratedGradients as tf_explain_IntegratedGradients

from xplainer.backend.tools.abstract_tf_explain_basic import AbstractTfExplainBasicTool


class IntegratedGradients(AbstractTfExplainBasicTool):
    def __init__(self):
        super().__init__(tf_explain_IntegratedGradients)

    def name(self):
        return "IntegratedGradients"

    def category(self):
        return "Gradient Based"
