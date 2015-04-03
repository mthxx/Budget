from setuptools import setup, find_packages

try:
    long_description = open("README.rst").read()
except IOError:
    long_description = ""

setup(
    name="budget",
    version="0.0.1",
    description="Personal Finance",
    license="GPL v2.0",
    author="Marc Thomas",
    author_email = "mat@mthx.org",
    url = "http://github.com/mthxx/budget",
    packages=find_packages(),
    include_package_data=True,
    install_requires=[],
    long_description=long_description,
    classifiers=[
        "Programming Language :: Python",
        "Programming Language :: Python :: 3.4",
    ]
)
