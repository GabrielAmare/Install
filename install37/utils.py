import os


def write(fp: str, content: str):
    with open(fp, mode="w", encoding="utf-8") as file:
        file.write(content.strip() + "\n")


def write_meta(name: str, version: tuple):
    write(os.path.join(name, "__meta__.py"), f"""
__version__ = ({version[0]}, {version[1]}, {version[2]})
""")


def write_requirements():
    write("requirements.txt", "")


def write_setup(name: str, author: str, author_email: str, description: str = ""):
    root = os.path.split(os.path.abspath(os.curdir))[-1]

    write("setup.py", f"""
from install37 import setup
from {name}.__meta__ import __version__

if __name__ == "__main__":
    setup(
        name="{name}",
        version=__version__,
        author="{author}", 
        author_email="{author_email}",
        description="{description}", 
        url="https://github.com/{author.replace(' ', '')}/{root}", 
        packages=["{name}"], 
        classifiers=[], 
        python_requires=">=3.7"
    )
""")
