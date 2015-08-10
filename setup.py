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
    version="0.0.10",
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
    data_files=[("/usr/share/applications/", ["PKGBUILD/budget.desktop"])
        ,("/usr/share/icons/hicolor/16x16/apps", ["PKGBUILD/budget-16/budget.png"])
        ,("/usr/share/icons/hicolor/24x24/apps", ["PKGBUILD/budget-24/budget.png"])
        ,("/usr/share/icons/hicolor/32x32/apps", ["PKGBUILD/budget-32/budget.png"])
        ,("/usr/share/icons/hicolor/48x48/apps", ["PKGBUILD/budget-48/budget.png"])
        ,("/usr/share/icons/hicolor/64x64/apps", ["PKGBUILD/budget-64/budget.png"])
        ,("/usr/share/icons/hicolor/128x128/apps", ["PKGBUILD/budget-128/budget.png"])
        ,("/usr/share/icons/hicolor/scalable/apps", ["PKGBUILD/budget-128/budget.svg"])
        ,("/usr/share/icons/Adwaita/16x16/apps", ["PKGBUILD/budget-16/budget.png"])
        ,("/usr/share/icons/Adwaita/24x24/apps", ["PKGBUILD/budget-24/budget.png"])
        ,("/usr/share/icons/Adwaita/32x32/apps", ["PKGBUILD/budget-32/budget.png"])
        ,("/usr/share/icons/Adwaita/48x48/apps", ["PKGBUILD/budget-48/budget.png"])
        ,("/usr/share/icons/Adwaita/64x64/apps", ["PKGBUILD/budget-64/budget.png"])
        ,("/usr/share/icons/Adwaita/128x128/apps", ["PKGBUILD/budget-128/budget.png"])
        ,("/usr/share/icons/Adwaita/scalable/apps", ["PKGBUILD/budget-128/budget.svg"])
        ],
    classifiers=[
        "Programming Language :: Python",
        "Programming Language :: Python :: 3.4",
    ]
)
