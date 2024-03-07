import os
import shutil
import time
import zipfile


def zip_directory_zip_file(directory_path, zip_path):
    with zipfile.ZipFile(zip_path, 'w', zipfile.ZIP_DEFLATED) as zipper:
        for root, dirs, files in os.walk(directory_path):
            for file in files:
                file_path = os.path.join(root, file)
                arc_name = os.path.relpath(file_path, directory_path)
                zipper.write(file_path, arc_name)


def zip_directory_shutils(directory_path, zip_path):
    shutil.make_archive(zip_path, format='zip', root_dir=directory_path)


if __name__ == '__main__':
    start = time.time()
    zip_directory_shutils('resources/bin', 'resources/bin.zip')
    print(f'Time taken: {time.time() - start}')

    if os.path.exists('resources/bin.zip'):
        os.remove('resources/bin.zip')
