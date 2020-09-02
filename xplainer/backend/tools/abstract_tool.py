from abc import ABC, abstractmethod
from typing import Union

import numpy as np
import tensorflow as tf

from xplainer.backend.utils.image import prepare_for_prediction


class GeneralSettings:
    results: int
    threshold: float

    def __init__(self, settings: dict):
        """

        :param settings:
        :raises KeyError, ValueError
        """
        self.results = int(settings["results"])
        self.threshold = float(settings["threshold"])


class AbstractTool(ABC):
    """
    Implement this class, save the file into the tools/ folder. And it will be registered and provided as a tool.
    """

    def id(self) -> str:
        """
        :return: unique string identifier
        """
        return self.__class__.__name__.lower()

    @abstractmethod
    def name(self) -> str:
        """
        :return: name of this tool
        """
        raise NotImplementedError

    @abstractmethod
    def category(self) -> str:
        """
        :return: name of a category of this tool
        """
        raise NotImplementedError

    def description(self) -> Union[str, None]:
        """
        :return: optional string description of this tool
        """
        return None

    @abstractmethod
    def source_name(self) -> str:
        """
        :return: name of the source of this tool's implementation
        """
        raise NotImplementedError

    @abstractmethod
    def source_url(self) -> str:
        """
        :return: URL of the source of this tool's implementation
        """
        raise NotImplementedError

    def tool_parameters(self) -> Union[dict, None]:
        """
        Describes parameters of a tool which can be set by user. The description is provided as a JSON.

        Structure contains two elements, list with the parameters and optional layout,
        which tells the user interface how to split the parameters into rows and what order to use.
        if not present, all parameters will be shown in one row, according the the order in which they were defined

        {
            "list": [
                {
                    "param": String <mandatory, key of the parameter>,
                    "name": String <mandatory, name of the parameter>,
                    "description": String <optional, serves as a help for the user>,
                    "type": String <mandatory, allowed values: int, float, bool>,
                    "default": int | float | bool <mandatory>,
                    "min": int | float <optional for given types>,
                    "max": int | float <optional for given types>,
                    "step": int | float <optional for given types, information for the user interface only>,
                },
               ... another parameters ...
            ],
            "layout" : [
               [...keys of params in the first row ...],
               [...keys of params in the second row...],
            ]
        }

        :return:
        """
        return None

    def explain(
        self, model: tf.keras.Model, image_path: str, general_settings: GeneralSettings, tool_settings: dict = None
    ) -> list:
        """
        Explain prediction for given model and image. The resulting dictionary should contain keys:
        - label_id: int
        - image: base64 encoded image

        Method is implemented for cases, when explaining is done one label after another.
        Provide content of explain_one()!
        Otherwise overwrite this method and you can ignore explain_one() method.

        :param model: model whose prediction we would like to explain
        :param image_path: image to be explained
        :param general_settings: common setup containing settings for every tool (number of images etc.)
        :param tool_settings: values for of a tool setup in the form of {parameter name: parameter value}
        :return: dictionary with the explanation
        """
        image = prepare_for_prediction(model, image_path)
        onehot, labels = self._get_labels(model, image, general_settings)

        tool_settings = tool_settings if tool_settings is not None else {}
        results = map(
            lambda label: {
                "label_id": int(label),
                "probability": float(onehot[label]),
                "image": self.explain_one(model, image_path, label, tool_settings),
            },
            labels,
        )
        return list(results)

    @staticmethod
    def _get_labels(model: tf.keras.Model, image: tf.Tensor, general_settings: GeneralSettings):
        onehot = model.predict(image)[0]

        over_threshold = np.sum(np.array(onehot) >= general_settings.threshold)
        results = np.min([general_settings.results, over_threshold])
        labels = np.argsort(onehot)[::-1][:results]
        return onehot, labels

    def explain_one(self, model: tf.keras.Model, image_path: str, label: int, tool_settings: dict) -> str:
        """
        If explaining is done one label by another, overwrite this method.
        The rest will be provided by explain() method. If this is not your case,
        overwrite explain() and ignore this method.

        :param model: model whose prediction we would like to explain
        :param image_path: image to be explained
        :param label: label to explain
        :param tool_settings: values for of a tool setup in the form of {parameter name: parameter value}
        :return: image explanation in base64 format
        """
        raise NotImplementedError

    def to_json(self, detail: bool = False) -> dict:
        """
        :param detail: True if we want to include the description and source in the detail;
                       false if id, name and category is wnough
        :return: JSON description of this tool
        """
        result = {
            "id": self.id(),
            "name": self.name(),
            "category": self.category(),
        }

        if detail:
            result = {
                **result,
                "description": self.description(),
                "source_name": self.source_name(),
                "source_url": self.source_url(),
                "parameters": self.tool_parameters(),
            }

        return result

    def process_parameters(self, user_params: dict) -> dict:
        """
        Takes user parameters and checks

        :param user_params: parameters user would like to change, does not need to contain all parameters of af a tool
        :return: dictionary of all parameters with provided or default values
        :raises ValueError if some parameter value is of a wrong type or does not respect min/max
        """

        def check_bounds(val, par):
            """
            Checks if given value is withing min / max of given parameter (if those are specified.)
            Raise ValueError if some condition is not met.
            """
            if "min" in par and val < par["min"]:
                raise ValueError(f"Invalid value {user_value} of {key}. Should be lower than or equal to {par['min']}.")

            if "max" in par and val > par["max"]:
                raise ValueError(
                    f"Invalid value {user_value} of {key}. Should be greater than or equal to {par['max']}."
                )

        if not self.tool_parameters() or "list" not in self.tool_parameters():
            return {}

        result = {}
        params = self.tool_parameters()["list"]
        for param in params:
            key = param["param"]
            user_value = user_params.get(key, None) if user_params else None

            # Value not present - that is OK, just use default.
            if not user_value:
                result[key] = param["default"]
                continue

            # Value is there, check if the type fits. In case min or max is applicable and defined, check it as well.
            # If not, do not try to hide it by using default, raise exception.
            required_type = param["type"]
            if required_type == "int" and isinstance(user_value, int):
                check_bounds(user_value, param)
                result[key] = user_value
                continue

            if required_type == "float" and (isinstance(user_value, float) or isinstance(user_value, int)):
                check_bounds(user_value, param)
                result[key] = float(user_value)
                continue

            if required_type == "bool" and isinstance(user_value, bool):
                result[key] = user_value
                continue

            raise ValueError(f"Invalid type {type(user_value)} of {key}. Should be {required_type}.")

        return result
