import os
import json
from .utils import write_init, write_meta, write_setup, write_requirements


def build(name: str, author: str, author_email: str, description: str = "", author_github: str = ""):
    """

    :param name: The project name
    :param root: The project location
    :return: None
    """

    if not os.path.exists(name):
        os.mkdir(name)
    else:
        raise FileExistsError("???", "can't rebuild a project to avoid overwriting", name)

    write_meta(
        name=name,
        version=(1, 0, 0)
    )
    write_init(
        name=name,
        description=description
    )
    write_setup(
        name=name,
        author=author,
        author_email=author_email,
        description=description,
        author_github=author_github
    )
    write_requirements()


def _get_author_metadata_fp():
    return os.path.join(os.path.expanduser("~"), "author_metadata.json")


def sbuild(name: str, description: str):
    """Simplified version of build, requires author-metadata.json present in the user home directory"""

    author_metadata_fp = _get_author_metadata_fp()

    if not os.path.exists(author_metadata_fp):
        raise FileNotFoundError(author_metadata_fp)

    with open(author_metadata_fp, mode="r", encoding="utf-8") as file:
        author_metadata = json.load(file)

    return build(name=name, description=description, **author_metadata)


def make_author_metadata(author: str, author_email: str, author_github: str):
    author_metadata_fp = _get_author_metadata_fp()

    if os.path.exists(author_metadata_fp):
        raise FileExistsError(author_metadata_fp)

    author_metadata = dict(
        author=author,
        author_email=author_email,
        author_github=author_github
    )

    with open(author_metadata_fp, mode="w", encoding="utf-8") as file:
        json.dump(author_metadata, file)
