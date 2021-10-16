from setuptools import setup


# Reading README.md file for long description
with open("README.md", "r", encoding="utf-8") as f:
    long_description = f.read()

setup(
    name="src",
    version="0.0.1",
    author="USER_NAME",
    description="A small package for dvc ml pipeline demo",
    long_description=long_description,
    long_description_content_type="text/markdown",
    url="https://github.com/subha996/DVC-ML-Demo",
    author_email="subhabratanath98@gmail.com",
    packages=["src"],
    python_requires=">=3.8",
    install_requires=[
        'dvc',
        'pandas',
        'sklearn'
    ]
)

