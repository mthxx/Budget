from setuptools import setup, find_packages

setup(
    name = "Budget",
    version = "0.1",
    description = "Personal Finance",
    author = "Marc Thomas",
    author_email = "mat at mthx dot org",
    url = "http://github.com/mthxx/budget",
    package_dir = {'budget' : 'budget'},
    #packages = ['budget'],
    package_data = {'budget':['*.png','*.css'],},
    packages=find_packages(),
    include_package_data=True,
    entry_points={'gui_scripts': ['budget = budget.budget:init']},
    license = "GPL v2.0",
    keywords = "budget finance mthx money",
)

