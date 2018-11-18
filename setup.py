import setuptools
import os

here = os.path.abspath(os.path.dirname(__file__))

# Get the long description from the README file
with open(os.path.join(here, 'README.md'), encoding='utf-8') as f:
    long_description = f.read()


with open(os.path.join(here, 'requirements'), encoding='utf-8') as f:
    requirements = f.read().splitlines()


setuptools.setup(
    name="bankreader",
    version="0.2.1",
    author="Alin BARBATEI",
    description="Romanian banks statement parser",
    long_description=long_description,
    license='MIT',
    long_description_content_type="text/markdown",
    url="https://github.com/abarbatei/bankreader",
    download_url='https://github.com/abarbatei/bankreader/archive/0.2.1.tar.gz',
    packages=setuptools.find_packages(exclude=['test']),
    install_requires=requirements,
    classifiers=[
        "Development Status :: 4 - Beta",
        "Programming Language :: Python :: 3",
        "License :: OSI Approved :: MIT License",
        "Operating System :: OS Independent",
    ],
)
