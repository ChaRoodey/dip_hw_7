import os
import zipfile as zf


def cr_zip(name_or, name_new: str) -> None:
    with zf.ZipFile(name_new, 'w', zf.ZIP_DEFLATED) as zipf:
        for root, dirs, files in os.walk(name_or):
            print(root, dirs, files)
            for file in files:
                file_path = os.path.join(root, file)
                zipf.write(file_path, os.path.relpath(file_path, name_or))


if __name__ == '__main__':
    cr_zip('C:/Users/Vlad/PycharmProjects/dip_hw_7/dir',
           'C:/Users/Vlad/PycharmProjects/dip_hw_7/dir.zip')
