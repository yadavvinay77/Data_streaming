# setup.py
from setuptools import setup, find_packages

setup(
    name="streaming_app",
    version="0.1.0",
    packages=find_packages("src"),
    package_dir={"":"src"},
    install_requires=[
        "pyspark>=3.4.0",
        "tabulate",
        "matplotlib",
        "numpy",
    ]
)
