import os

import numpy as np
import tensorflow as tf


def get_params_count(model: tf.keras.Model) -> int:
    """
    Calculate number of variable in a model.

    :param model: TensorFlow Keras model.
    :return: number of variables
    """
    variables = model.variables
    return sum(map(lambda v: np.prod(v.shape), variables))


def is_flat(model: tf.keras.Model) -> bool:
    """
    :param model: TensorFlow Keras model.
    :return: true if there is another model among given model layers
    """
    for layer in model.layers:
        if isinstance(layer, tf.keras.Model):
            return False

    return True


def get_input_shape(model: tf.keras.Model):
    """
    :param model: TensorFlow Keras model.
    :return: Input shape (height, width, channels) of given model.
    """
    return model.input.shape[1:]


def get_size(model: tf.keras.Model, default=512):
    """
    :param model: TensorFlow Keras model.
    :param default: Default size if any of the dimensions is not defined.
    :return: (height, width) couple of an input image for given model.
    """
    shape = get_input_shape(model)
    size = shape[0:2]
    size = tuple((s if s is not None else default) for s in size)

    return size


def load_and_analyze(model_path: str, tmp_dir):
    model = tf.keras.models.load_model(model_path)

    # TODO plot_model might not work because graphviz is not installed on the system (pip package is not enough)
    model_plot_path = os.path.join(tmp_dir, "model_plot.png")
    tf.keras.utils.plot_model(
        model,
        to_file=model_plot_path,
        show_shapes=True,
        show_layer_names=True,
        rankdir="TB",
        expand_nested=True,
        dpi=70,
    )

    return model
