from install37 import make_author_metadata, sbuild

if __name__ == '__main__':
    # First I create my metadata file, which the program will read to build my projects
    make_author_metadata(
        author="Gabriel Amare",
        author_email="gabriel.amare.dev@gmail.com",
        author_github="https://github.com/GabrielAmare"
    )

    # Then I init the current project 'install37'
    sbuild(
        name="install37",
        description="Install tool for python apps"
    )
