from setuptools import setup, find_packages

__version__ = "1.0"
setup(
    name="coding-interview",
    version=__version__,
    python_requires="~=3.7",
    install_requires=[
        "numpy==1.21.4",
    ],
    extras_require={
        "tests": [
            "black~=20.8b1",
            "mypy~=0.910",
            "pytest~=6.2.5",
            "pytest-cov~=3.0.0",
        ]
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
