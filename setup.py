from setuptools import setup, find_packages

try:
    long_description = open("README.rst").read()
except IOError:
    long_description = ""

ENTRY_POINTS = {
    'console_scripts': ['budget=budget.budget:main'],
    #gui_scripts=['app_gui=budget.buget:start']
}


setup(
    name="budget",
    version="0.0.2",
    description="Personal Finance",
    license="GPL v2.0",
    author="Marc Thomas",
    author_email = "mat@mthx.org",
    url = "http://github.com/mthxx/budget",
    packages=find_packages(),
    include_package_data=True,
    install_requires=[],
    long_description=long_description,
    entry_points=ENTRY_POINTS,
    classifiers=[
        "Programming Language :: Python",
        "Programming Language :: Python :: 3.4",
    ]
)
