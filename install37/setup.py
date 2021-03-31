import os
import sys
import setuptools
import pkg_resources
from .utils import write_meta


def setup(name, version, author, author_email, description, url, packages, classifiers, python_requires,
          update_type="patch"):
    sys.argv.append("sdist")
    sys.argv.append("bdist_wheel")

    with open("README.md", "r", encoding="utf-8") as fh:
        long_description = fh.read()

    with open("requirements.txt", "r", encoding="utf-8") as fh:
        requirements = list(map(str, pkg_resources.parse_requirements(fh.read())))

    setuptools.setup(
        name=name,
        version=f"{version[0]}.{version[1]}.{version[2]}",
        author=author,
        author_email=author_email,
        description=description,
        long_description=long_description,
        long_description_content_type="text/markdown",
        install_requires=requirements,
        url=url,
        packages=packages,
        classifiers=classifiers,
        python_requires=python_requires,
    )

    python_dir = os.path.dirname(sys.executable) + "\\python.exe"
    os.system(python_dir + ' -m twine upload --repository testpypi dist/*')

    if update_type == "patch":
        write_meta(name=name, version=(version[0], version[1], version[2] + 1))
    elif update_type == "minor":
        write_meta(name=name, version=(version[0], version[1] + 1, 0))
    elif update_type == "major":
        write_meta(name=name, version=(version[0] + 1, 0, 0))
    else:
        raise ValueError(update_type)
