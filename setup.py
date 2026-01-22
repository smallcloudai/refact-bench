from setuptools import setup, find_packages

setup(
    name="refact-scenarios",
    version="0.1.0",
    packages=find_packages(),
    include_package_data=True,
    install_requires=[
        "PyYAML~=6.0.2",
        "requests~=2.32.3",
        "setuptools~=68.2.0",
        "wheel>=0.46.2",
        "docker~=7.1.0",
        "GitPython~=3.1.43",
        "refact",
        "asgiref",
        "pydantic~=2.9.2",
        "pandas",
        "colorama",
        "pyarrow",
        "fsspec",
        "huggingface_hub"
    ],
    classifiers=[
        "Development Status :: 3 - Alpha",
        "Intended Audience :: Developers",
        "License :: OSI Approved :: MIT License",
        "Programming Language :: Python :: 3",
        "Programming Language :: Python :: 3.7",
        "Programming Language :: Python :: 3.8",
        "Programming Language :: Python :: 3.9",
        "Programming Language :: Python :: 3.10",
    ],
    python_requires=">=3.7",
    entry_points={
        'console_scripts': [
            'fakeide=refact_scenarios.fakeide:main',
        ],
    },
)
