from setuptools import find_packages, setup

__version__ = "1.0"
setup(
    name="coding-interview",
    version=__version__,
    python_requires=">=3.9,<3.12",
    install_requires=[
        "numpy==1.26.2",
    ],
    extras_require={
        "lint": [
            "black==23.12.1",
            "isort==5.13.2",
            "pre-commit==3.3.3",
            "flake8==6.1.0",
            "mypy==1.8.0",
        ],
        "tests": [
            "pytest==7.4.0",
            "pytest-cov==4.1.0",
        ],
    },
    packages=find_packages("src", exclude=["*.tests", "*.tests.*", "tests.*", "tests"]),
    package_dir={"": "src"},
    include_package_data=True,
    description="coding interview problems and solutions",
    license="MIT",
    author="seahrh",
    author_email="seahrh@gmail.com",
    url="https://github.com/seahrh/coding-interview",
)
