import setuptools
from setuptools import find_packages

with open('readme.md', mode="r") as rmfile:
	long_description = rmfile.read()

setuptools.setup(
	author="Ritesh Bhat",
	author_email="hackslanger@zoho.com",
	name="py_profiler",
	python_requires=">=3.4",
	packages=find_packages(),
	description="Simple library for python code profiling",
	long_description=long_description,
	long_description_content_type="text/markdown",
	url="https://github.com/hackSlanger/py-profiler"
)
