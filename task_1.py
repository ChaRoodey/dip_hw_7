import os


def group_rename(name: str, num: int, ext_or, ext_new: str, diap: list):
    d = os.listdir()

    for i in range(len(d)):
        if ext_or in d[i]:
            new_name = (d[i])[diap[0]:diap[1] + 1] + str(i) + ext_new
            os.rename(d[i], new_name)


if __name__ == '__main__':
    group_rename('new.txt', 1, '.txt', '.txt', [0,2])