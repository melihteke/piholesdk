from setuptools import setup, find_packages

setup(
    name="piholesdk",
    version="0.1.0",
    packages=find_packages(),
    author="Melih Teke",
    author_email="me@mteke.com",
    description="A Python client for managing DNS records on a Pi-hole server via SSH.",
    long_description=open('README.md').read(),
    long_description_content_type="text/markdown",
    url="https://github.com/melihteke/piholesdk.git",
    classifiers=[
        "Programming Language :: Python :: 3",
        "License :: OSI Approved :: MIT License",
        "Operating System :: OS Independent",
    ],
    python_requires='>=3.6',
    install_requires=[
        'paramiko',
    ],
)