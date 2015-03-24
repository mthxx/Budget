from setuptools import setup, find_packages
setup(
    name = "Budget",
    version = "0.1",
    packages = find_packages(),
    scripts = ['budget','add_category_popover.py','data.py','add_popover.py','add_popover.py',
                'projections.py','calc.py','edit_popover.py','transactions.py',
                'overview.py','overview_menu.py','reports.py','window.py'],
    package_data = {'':['*.png','*.css'],},
    include_package_data=True,
    #install_requires = ['gtk3'],
    author = "Marc Thomas",
    author_email = "mat at mthx dot org",
    description = "Personal Finance",
    license = "GPL v2.0",
    keywords = "budget finance mthx money",
    url = "http://github.com/mthxx/budget"
)

