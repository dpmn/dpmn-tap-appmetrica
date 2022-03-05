#!/usr/bin/env python
from setuptools import setup

setup(
    name="tap-appmetrica",
    version="0.1.0",
    description="DPMN tap for extracting data",
    author="",
    url="",
    classifiers=["Programming Language :: Python :: 3 :: Only"],
    py_modules=["tap_appmetrica"],
    install_requires=[
        # NB: Pin these to a more specific version for tap reliability
        "requests",
    ],
    entry_points="""
    [console_scripts]
    tap-appmetrica=tap_appmetrica:main
    """,
    packages=["tap_appmetrica"],
    package_data = {
        "schemas": ["tap_appmetrica/schemas/*.json"]
    },
    include_package_data=True,
)
