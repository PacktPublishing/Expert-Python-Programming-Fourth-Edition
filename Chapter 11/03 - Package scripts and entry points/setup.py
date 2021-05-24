from setuptools import setup

setup(
    name="findimports",
    version="0.0.0",
    py_modules=["findimports"],
    entry_points={"console_scripts": ["findimports=findimports:main"]},
)
