from setuptools import setup

with open("README.md", "r", encoding="utf-8") as f:
    long_description = f.read()

## edit below variables as per your requirements -
REPO_NAME = "NextPage Guru Book Recommender System"
AUTHOR_USER_NAME = "Guru-NextPage"
SRC_REPO = "src"
LIST_OF_REQUIREMENTS = ["streamlit", "numpy"]


setup(
    name=SRC_REPO,
    version="0.0.1",
    author=AUTHOR_USER_NAME,
    description="A small package for Book Recommender System",
    long_description=long_description,
    long_description_content_type="text/markdown",
    url=f"https://github.com/Brijesh03032001/{REPO_NAME}",
    author_email="sainibrijesh01@gmail.com",
    packages=[SRC_REPO],
    license="MIT",
    python_requires=">=3.7",
    install_requires=LIST_OF_REQUIREMENTS,
)
