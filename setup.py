import setuptools

with open("requirements.txt") as f:
    install_requirements = f.read().splitlines()

long_description = """
The ultimate goal of this toolkit is to promote explainable AI. 
It should offer developers varied ways to examine predictions of their models.

We are just at the beginning of a long road. For a start, we decided to aim at:
- Image classification.
- Tensorflow 2+ models.

There are already a couple of existing libraries. We do not want to duplicate them.
This project rather tries to make them available with as little effort as possible,
at one place.

For more information, please visit the [GitHub repository](https://github.com/liborvaneksw/xplainer/).
"""

setuptools.setup(
    name="xplainer",
    version="0.0.2",
    author="Libor Vanek",
    author_email="libor@xplainer.ai",
    description="xplainer.ai toolkit enables developers to explore predictions "
    "of their deep learning models. Focused on image classification and TensorFlow 2+. ",
    long_description=long_description,
    long_description_content_type="text/markdown",
    url="https://github.com/liborvaneksw/xplainer",
    classifiers=[
        "Programming Language :: Python :: 3",
        "License :: OSI Approved :: MIT License",
        "Operating System :: OS Independent",
    ],
    python_requires=">=3.6",
    packages=setuptools.find_packages(),
    install_requires=install_requirements,
    zip_safe=False,
    include_package_data=True,
    scripts=["bin/xplainer"],
)
