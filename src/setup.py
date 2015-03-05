from setuptools import setup, find_packages
setup(
    name = "Budget",
    version = "0.1",
    packages = find_packages(),
    scripts = ['Budget.py'],

    # Project uses reStructuredText, so ensure that the docutils get
    # installed or upgraded on the target machine
    # install_requires = ['docutils>=0.3'],

    #package_data = {
        # If any package contains *.txt or *.rst files, include them:
    #    '': ['*.txt', '*.rst'],
        # And include any *.msg files found in the 'hello' package, too:
    #    'hello': ['*.msg'],
    #},

    # metadata for upload to PyPI
    author = "Marc Thomas",
    author_email = "mat@mthx.org",
    description = "Personal Finance",
    license = "GPL v2.0",
    keywords = "budget finance mthx money",
    url = "http://github.com/mthx_/budget"   # project home page, if any

    # could also include long_description, download_url, classifiers, etc.
)

