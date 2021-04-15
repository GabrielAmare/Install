import os


def indent(text: str, prefix: str = "    "):
    return "\n".join(prefix + line for line in text.split("\n"))


def write(fp: str, content: str):
    with open(fp, mode="w", encoding="utf-8") as file:
        file.write(content.strip() + "\n")


def write_meta(name: str, version: tuple):
    write(os.path.join(name, "__meta__.py"), f"""
__version__ = ({version[0]}, {version[1]}, {version[2]})
""")


def write_init(name: str, description: str):
    write(os.path.join(name, "__init__.py"), f"""
\"\"\"
{name} :
{indent(description)}
\"\"\"
""")


def write_requirements():
    write("requirements.txt", "")


def write_setup(name: str, author: str, author_email: str, description: str = "", author_github: str = ""):
    root = os.path.split(os.path.abspath(os.curdir))[-1]

    if not author_github:
        author_github = f"https://github.com/{author.replace(' ', '')}"

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
        url="{author_github}/{root}", 
        packages=["{name}"], 
        classifiers=[], 
        python_requires=">=3.7"
    )
""")
