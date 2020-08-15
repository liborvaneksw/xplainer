import base64
from functools import singledispatch

import cv2
import numpy as np
import tensorflow as tf

from xplainer.backend.utils.model import get_size


@singledispatch
def get_base64png(image) -> str:
    """
    :param image: image path, numpy array or tensor
    :return: given image encoded in base64 png, including the type prefix
    """
    raise TypeError(f"Unknown type {type(image)}")


@get_base64png.register(str)
def _(img_path: str) -> str:
    img_png = tf.io.read_file(img_path)
    return _get_base64png(img_png)


@get_base64png.register(np.ndarray)
def _(img_numpy: np.ndarray) -> str:
    if len(img_numpy.shape) == 2:
        img_numpy = tf.image.grayscale_to_rgb(tf.expand_dims(img_numpy, -1))
    img_png = tf.image.encode_png(img_numpy)
    return _get_base64png(img_png)


@get_base64png.register(tf.Tensor)
def _(img_tensor: tf.Tensor) -> str:
    return get_base64png(img_tensor.numpy())


def _get_base64png(img_png) -> str:
    image_base46 = "data:image/png;base64," + base64.b64encode(img_png.numpy()).decode("utf-8")
    return image_base46


def prepare_for_prediction(model: tf.keras.Model, image_path: str, expand_dims=True) -> tf.Tensor:
    """
    Takes an image path, loads the image a prepares it for a prediction with a given model. The model is used to get
    the input dimensions of an image.

    :param model: model which will be later used for predictions on given image
    :param image_path: path to the image
    :param expand_dims: whether we should create a batch from the image by adding one dimension
    :return: image Tensor ready to be used for prediction
    """
    size = get_size(model)

    image_encoded = tf.io.read_file(image_path)
    image = tf.io.decode_image(image_encoded, channels=3)

    image = tf.image.convert_image_dtype(image, tf.float32, saturate=True)
    image = tf.image.resize(image, size)

    if expand_dims:
        image = tf.expand_dims(image, 0)

    return image


def create_thumbnail(img_bytes: bytes, size: int = 100) -> np.ndarray:
    """
    :param img_bytes: image represented as bytes, in any standard format
    :param size: size of a longer size of a thumbnail
    :return: thumbnail represented as a numpy array
    """
    image_thumbnail = np.asarray(bytearray(img_bytes), dtype=np.uint8)
    image_thumbnail = cv2.imdecode(image_thumbnail, cv2.IMREAD_COLOR)
    (h, w) = image_thumbnail.shape[:2]
    scale = min(size / h, size / w)
    image_thumbnail = cv2.resize(image_thumbnail, (int(w * scale), int(h * scale)))
    return image_thumbnail
