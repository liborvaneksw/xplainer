from tf_explain.core import IntegratedGradients as tf_explain_IntegratedGradients

from xplainer.backend.tools.abstract_tf_explain_basic import AbstractTfExplainBasicTool


class IntegratedGradients(AbstractTfExplainBasicTool):
    def __init__(self):
        super().__init__(tf_explain_IntegratedGradients)

    def name(self):
        return "Integrated Gradients"

    def category(self):
        return "Gradient Based"

    def tool_parameters(self) -> dict:
        return {
            "list": [
                {
                    "param": "n_steps",
                    "name": "Steps",
                    "type": "int",
                    "default": 20,
                    "min": 1,
                    "max": 1000,
                    "step": 1,
                }
            ]
        }
