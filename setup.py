import setuptools

with open("README.md", "r") as fh:
    long_description = fh.read()

setuptools.setup(
    name="bankreader",
    version="0.0.2",
    author="Alin BARBATEI",
    author_email="alin.barbatei@gmail.com",
    description="Romanian bank statement parser",
    long_description=long_description,
    long_description_content_type="text/markdown",
    url="https://github.com/abarbatei/bankreader",
    packages=setuptools.find_packages(),
    classifiers=[
        "Programming Language :: Python :: 3",
        "License :: OSI Approved :: MIT License",
        "Operating System :: OS Independent",
    ],
)