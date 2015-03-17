from setuptools import setup, find_packages
setup(
    name = "Budget",
    version = "0.1",
    packages = find_packages(),
    scripts = ['budget'],
    install_requires = ['gtk3'],
    author = "Marc Thomas",
    author_email = "mat at mthx dot org",
    description = "Personal Finance",
    license = "GPL v2.0",
    keywords = "budget finance mthx money",
    url = "http://github.com/mthxx/budget"
)

