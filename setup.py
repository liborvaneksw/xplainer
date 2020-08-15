import setuptools

with open("README.md", "r") as fh:
    long_description = fh.read()

with open("requirements.txt") as f:
    install_requirements = f.read().splitlines()

setuptools.setup(
    name="xplainer toolkit",
    version="0.0.1",
    author="Libor Vanek",
    author_email="libor@xplainer.ai",
    description="Explainable AI made easy. Simple browser based app that enables user "
                + "to explore their computer vision TensorFlow models predictions.",
    long_description=long_description,
    long_description_content_type="text/markdown",
    url="https://github.com/liborvaneksw/xplainer",
    classifiers=[
        "Programming Language :: Python :: 3",
        "License :: OSI Approved :: MIT License",
        "Operating System :: OS Independent",
    ],
    python_requires='>=3.6',
    packages=setuptools.find_packages(),
    install_requires=install_requirements,
    zip_safe=False,
    include_package_data=True,
    scripts=['bin/xplainer'],
)
