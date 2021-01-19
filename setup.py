import setuptools

with open("README.md", "r") as fh:
    long_description = fh.read()

setuptools.setup(
    name="stackbuilder",
    version="0.1",
    author="Travis Delly",
    author_email="tdellytech@gmail.com",
    description="Transforms cloud formation resource files into one giant file",
    long_description=long_description,
    url="https://github.com/dellybro",
    packages=setuptools.find_packages(),
    entry_points={
        "console_scripts": ["stackbuilder-py=stackbuilder.__main__:cli"],
    },
    classifiers=[
        "Programming Language :: Python :: 3",
        "License :: OSI Approved :: MIT License",
        "Operating System :: OS Independent"
    ]

)