from setuptools import setup, find_packages

setup(
    name="FirstAgentHugginface",
    version="0.1.0",
    packages=find_packages(exclude=["tests*", "venv", ".venv"]),
    install_requires=[
        "markdownify",
        "smolagents==1.8.1",
        "requests",
        "duckduckgo_search",
        "pandas",
        "gradio",
        "pytz",
        "PyYAML"
        "PdfReader"
    ],
    include_package_data=True,
)