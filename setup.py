from setuptools import setup, find_packages

setup(
    name="mirror-log",
    version="0.1.0",
    author="abhikashyap",
    author_email="abhikashyap10@gmail.com",
    description="A custom Python logger that mirrors the caller's file structure.",
    long_description=open('README.md').read(),
    long_description_content_type="text/markdown",
    url="https://github.com/abhikashyap/mirror-log",
    packages=find_packages(where="src"),
    package_dir={"": "src"},
    classifiers=[
        "Programming Language :: Python :: 3",
        "License :: OSI Approved :: MIT License",
        "Operating System :: OS Independent",
    ],
    python_requires='>=3.6',
)
