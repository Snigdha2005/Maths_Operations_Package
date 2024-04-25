import setuptools

with open("README.md", "r", encoding = "utf-8") as fh:
    long_description = fh.read()

setuptools.setup(
    name = "Mathematical_Operations",
    version = "0.0.1",
    author = "Snigdha2005",
    author_email = "YS.Snigdha@iiitb.ac.in",
    description = "Basic mathematical operations",
    long_description = long_description,
    long_description_content_type = "text/markdown",
    url = "https://github.com/Snigdha2005/mathematical_operations",
    classifiers = [
        "Programming Language :: Python :: 3",
        "License :: OSI Approved :: MIT License",
        "Operating System :: OS Independent",
    ],
    package_dir = {"": "src"},
    packages = setuptools.find_packages(where="src"),
    python_requires = ">=3.6"
    )

