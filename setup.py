from setuptools import setup

import os


def get_packages(package):
    """
    Return root package and all sub-packages.
    """
    return [
        dirpath
        for dirpath, dirnames, filenames in os.walk(package)
        if os.path.exists(os.path.join(dirpath, "__init__.py"))
    ]


setup(
    name="linkibot",
    python_requires=">=3.6",
    url="https://github.com/ycd/linkibot",
    license="BSD",
    author="Yagiz Degirmenci",
    packages=get_packages("linkibot"),
    package_data={"starlette": ["py.typed"]},
    include_package_data=True,
    extras_require={
        "full": [
            "selenium",
            "urllib3",
            "chromedriver-autoinstaller",
        ]
    },
    classifiers=[
        "Programming Language :: Python :: 3",
        "Programming Language :: Python :: 3.6",
        "Programming Language :: Python :: 3.7",
        "Programming Language :: Python :: 3.8",
        "Programming Language :: Python :: 3.9",
    ],
    zip_safe=False,
)