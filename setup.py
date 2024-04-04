from setuptools import setup, find_packages

with open('README.md', 'r', encoding='utf-8') as fh:
    long_description = fh.read()

setup(
    name="piholesdk",
    version="0.1.3",
    packages=find_packages(),
    author="Melih Teke",
    author_email="me@mteke.com",
    description="A Python client for managing DNS records on a Pi-hole server via SSH.",
    long_description=f"{long_description}\n\nFor more information, visit the [PyPI page](https://pypi.org/project/piholesdk/).\n\nYou can also connect with me on [LinkedIn](https://www.linkedin.com/in/melih-teke/).",
    long_description_content_type='text/markdown',
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
