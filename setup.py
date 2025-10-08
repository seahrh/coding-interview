from setuptools import find_packages, setup

__version__ = "1.0"
setup(
    name="coding-interview",
    version=__version__,
    python_requires=">=3.11,<3.13",
    install_requires=[
        "numpy==1.26.4",
    ],
    extras_require={
        "lint": [
            "black==25.1.0",
            "isort==6.0.1",
            "pre-commit==4.2.0",
            "flake8==7.3.0",
            "mypy==1.16.1",
        ],
        "tests": [
            "pytest==8.3.3",
            "pytest-cov==6.0.0",
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
