import os
import time


def del_old_files(dir_name: str, days: int) -> None:
    sec = days * 24 * 60 * 60
    edge = time.time() - sec
    for root, dirs, files in os.walk(dir_name):
        for file in files:
            file_path = os.path.join(root, file)
            if os.path.getmtime(file_path) < edge:
                os.remove(file_path)


if __name__ == '__main__':
    del_old_files('dir', 2)