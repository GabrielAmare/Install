from install37 import setup
from install37.__meta__ import __version__

if __name__ == "__main__":
    setup(
        name="install37",
        version=__version__,
        author="Gabriel Amare", 
        author_email="gabriel.amare.31@gmail.com",
        description="Install tool for python apps", 
        url="https://github.com/GabrielAmare/Install", 
        packages=["install37"], 
        classifiers=[], 
        python_requires=">=3.7"
    )
