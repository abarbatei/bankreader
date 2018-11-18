import setuptools

with open("README.md", "r") as fh:
    long_description = fh.read()

with open("requirements", "r") as fh:
    requirements = fh.read().splitlines()


setuptools.setup(
    name="bankreader",
    version="0.2.0",
    author="Alin BARBATEI",
    description="Romanian banks statement parser",
    long_description=long_description,
    license='MIT',
    long_description_content_type="text/markdown",
    url="https://github.com/abarbatei/bankreader",
    download_url='https://github.com/abarbatei/bankreader/archive/0.2.0.tar.gz',
    packages=setuptools.find_packages(exclude=['test']),
    install_requires=requirements,
    classifiers=[
        "Development Status :: 4 - Beta",
        "Programming Language :: Python :: 3",
        "License :: OSI Approved :: MIT License",
        "Operating System :: OS Independent",
    ],
)
