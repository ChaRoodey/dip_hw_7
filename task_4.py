import os


def get_file(dir_name, file_end: str) -> None:
    for root, dirs, files in os.walk(dir_name):
        for file in files:
            if str.endswith(file, file_end):
                print(os.path.join(root, file))


if __name__ == '__main__':
    get_file('dir', 'txt')