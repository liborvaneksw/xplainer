from tf_explain.core import VanillaGradients as tf_explain_VanillaGradients

from xplainer.backend.tools.abstract_tf_explain_basic import AbstractTfExplainBasicTool


class VanillaGradients(AbstractTfExplainBasicTool):
    def __init__(self):
        super().__init__(tf_explain_VanillaGradients)

    def name(self):
        return "Vanilla Gradient"

    def category(self):
        return "Gradient Based"
