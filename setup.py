from setuptools import setup, find_packages

setup(
    name="opencode-custom-logger",
    version="0.1.0",
    author="Abhishek kumar",
    author_email="abhikashyap10@gmail.com",
    description="A custom Python logger that mirrors the caller's file structure.",
    long_description=open('README.md').read(),
    long_description_content_type="text/markdown",
    url="https://github.com/yourusername/opencode-custom-logger",
    packages=find_packages(where="src"),
    package_dir={"": "src"},
    classifiers=[
        "Programming Language :: Python :: 3",
        "License :: OSI Approved :: MIT License",
        "Operating System :: OS Independent",
    ],
    python_requires='>=3.6',
)
