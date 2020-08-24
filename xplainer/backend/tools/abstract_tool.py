from abc import ABC, abstractmethod
from typing import Union

import numpy as np
import tensorflow as tf

from xplainer.backend.utils.image import prepare_for_prediction


class GeneralSetup:
    results: int
    threshold: float

    def __init__(self, setup: dict):
        self.results = int(setup["results"])
        self.threshold = float(setup["threshold"])


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

    def explain(self, model: tf.keras.Model, image_path: str, general_setup: GeneralSetup) -> list:
        """
        Explain prediction for given model and image. The resulting dictionary should contain keys:
        - label_id: int
        - image: base64 encoded image

        :param model: model whose prediction we would like to explain
        :param image_path: image to be explained
        :param general_setup: common setup containing settings for every tool (number of images etc.)
        :return: dictionary with the explanation
        """
        image = prepare_for_prediction(model, image_path)

        onehot = model.predict(image)[0]
        over_threshold = np.sum(np.array(onehot) >= general_setup.threshold)
        results = np.min([general_setup.results, over_threshold])
        labels = np.argsort(onehot)[::-1][:results]

        results = map(
            lambda label: {
                "label_id": int(label),
                "probability": float(onehot[label]),
                "image": self.explain_one(model, image_path, label),
            },
            labels,
        )
        return list(results)

    @abstractmethod
    def explain_one(self, model: tf.keras.Model, image_path: str, label: int) -> dict:
        """

        :param model:
        :param image_path:
        :param label:
        :return:
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
            }

        return result
