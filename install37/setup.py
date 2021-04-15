import os
import sys
import time
import shutil
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

    major, minor, patch = version

    if update_type == "patch":
        patch += 1
    elif update_type == "minor":
        patch = 0
        minor += 1
    elif update_type == "major":
        patch = 0
        minor = 0
        major += 1
    else:
        raise ValueError(update_type)

    write_meta(name=name, version=(major, minor, patch))

    time.sleep(2)
    os.system(python_dir + f" -m pip install --force-reinstall -i https://test.pypi.org/simple/ {name}=={version[0]}.{version[1]}.{version[2]}")

    shutil.rmtree("dist")
    shutil.rmtree("build")
    shutil.rmtree(f"{name}.egg-info")
