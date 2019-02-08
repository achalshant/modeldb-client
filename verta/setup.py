from setuptools import setup

setup(
    name="verta",
    version="0.4.3",
    packages=[
        "verta",
        "verta.protos.modeldb",
    ],
    install_requires=[
        "grpcio==1.17.1",
        "protobuf==3.6.1",
        "requests==2.21.0",
    ],
)
