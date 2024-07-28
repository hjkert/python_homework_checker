import os
import filecmp
import difflib


def compare_folders(folder1, folder2):
    files1 = set(os.listdir(folder1))
    files2 = set(os.listdir(folder2))

    common_files = files1.intersection(files2)
    only_in_folder1 = files1 - files2
    only_in_folder2 = files2 - files1

    print(f"Files only in {folder1}: {only_in_folder1}")
    print(f"Files only in {folder2}: {only_in_folder2}")
    print("Comparing common files:")

    for file in common_files:
        path1 = os.path.join(folder1, file)
        path2 = os.path.join(folder2, file)

        if os.path.isfile(path1) and os.path.isfile(path2):
            if files_are_equal(path1, path2):
                print(f"{file}: Identical")
            else:
                print(f"{file}: Different")
                show_diff(path1, path2)
        else:
            print(f"{file}: Not a file in one or both locations")


def files_are_equal(file1, file2):
    with open(file1, 'r') as f1, open(file2, 'r') as f2:
        content1 = f1.read().rstrip('\r\n')
        content2 = f2.read().rstrip('\r\n')
        return content1 == content2


def show_diff(file1, file2):
    with open(file1, 'r') as f1, open(file2, 'r') as f2:
        diff = difflib.unified_diff(
            [line.rstrip('\r\n') for line in f1.readlines()],
            [line.rstrip('\r\n') for line in f2.readlines()],
            fromfile=file1,
            tofile=file2,
        )
        for line in diff:
            print(line)

