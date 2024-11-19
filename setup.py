from setuptools import setup, find_packages

setup(
    name="4tu-codepublish",
    version="0.1.0",
    packages=find_packages(),
    install_requires=[
        "certifi==2024.8.30",
        "charset-normalizer==3.4.0",
        "idna==3.10",
        "prompt-toolkit==3.0.36",
        "python-dotenv==1.0.1",
        "questionary==2.0.1",
        "requests==2.32.3",
        "urllib3==2.2.3",
        "wcwidth==0.2.13"
    ],
    entry_points={
        "console_scripts": [
                '4tu-codepublish = _4tu_codepublish._4tu_codepublish:main'
            ],
    },
    description="A brief description of your program",
    author="Jori van Dam",
    author_email="j.van.dam@issc.leidenuniv.nl",
    url="https://github.com/JDDevISSC/4TU-CodePublish",
    classifiers=[
        "Programming Language :: Python :: 3",
        "License :: OSI Approved :: MIT License",
        "Operating System :: OS Independent",
    ],
    python_requires=">=3.6",
)