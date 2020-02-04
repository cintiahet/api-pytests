from os.path import join, dirname


def load_file(filename, route):
    relative_path = join(route, filename)
    absolute_path = join(dirname(__file__), relative_path)

    with open(absolute_path) as file:
        return file.read()
