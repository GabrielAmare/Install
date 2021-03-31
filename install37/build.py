import os
from .utils import write_meta, write_setup, write_requirements


def build(name: str, author: str, author_email: str, description: str = ""):
    """

    :param name: The project name
    :param root: The project location
    :return: None
    """

    if not os.path.exists(name):
        os.mkdir(name)
    else:
        raise FileExistsError("???", "can't rebuild a project to avoid overwriting", name)

    write_meta(name=name, version=(1, 0, 0))
    write_setup(name=name, author=author, author_email=author_email, description=description)
    write_requirements()
