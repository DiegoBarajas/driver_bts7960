from setuptools import setup, find_packages
import codecs
import os

here = os.path.abspath(os.path.dirname(__file__))

with codecs.open(os.path.join(here, "README.md"), encoding="utf-8") as fh:
    long_description = "\n"+fh.read()

VERSION = "0.0.1"
DESCRIPTION = "Project to manage H-Brigde model BTS7960 with ESP32 on micropython"

# Setting up
setup(
    name="bts7960-micropython",
    version=VERSION,
    author="desaubv (Diego Barajas)",
    author_email="desaubv@gmail.com",
    description=DESCRIPTION,
    long_description_content_type="text/markdown",
    long_description=long_description,
    packages=find_packages(),
    install_requires=[],
    keywords=["micropython", 'electronics', 'esp32', 'hbridge', 'h-bridge', 'bts7960'],
    classifiers=[
        'Development Status :: 1 - Planning',
        'Intended Audience :: Developers',
        'Programming Language :: Python :: Implementation :: MicroPython',
    ],
)