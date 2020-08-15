from abc import ABC, abstractmethod
from typing import Union

import tensorflow as tf


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

    @abstractmethod
    def explain(self, model: tf.keras.Model, image_path: str) -> dict:
        """
        Explain prediction for given model and image. The resulting dictionary should contain keys:
        - label_id: int
        - image: base64 encoded image

        :param model: model whose prediction we would like to explain
        :param image_path: image to be explained
        :return: dictionary with the explanation
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
