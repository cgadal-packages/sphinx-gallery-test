from setuptools import find_packages, setup

setup(
    name="mytoolbox",
    packages=find_packages(),
    python_requires=">=3",
    install_requires=[
        "numpy",
        "matplotlib",
        "sphinx",
        "sphinx-gallery",
        "sphinx-autodoc-typehints",
        "pydata_sphinx_theme==0.16.1",
        "numpydoc",
    ],
    url="https://github.com/cgadal-packages/sphinx-gallery-test",
    author="Cyril Gadal",
    license="Apache-2.0",
    version="0.2",
    zip_safe=False,
)
