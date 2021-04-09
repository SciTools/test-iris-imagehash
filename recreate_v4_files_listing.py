#!/usr/bin/env python

import os
import os.path
from glob import glob


REPO_MAIN_DIRPATH = os.path.dirname(os.path.abspath(__file__))
V4_DIR = os.sep.join([REPO_MAIN_DIRPATH, "images", "v4"])
V4_LISTFILE_NAME = "v4_files_listing.txt"
V4_LISTFILE_PATH = os.sep.join([REPO_MAIN_DIRPATH, V4_LISTFILE_NAME])


def get_v4_imagefile_names(search_dirpath=V4_DIR, filespec="*.png"):
    """Return a list of the current image files in the v4 subdirectory."""
    files_spec = os.path.join(search_dirpath, filespec)
    file_paths = glob(files_spec)
    return [os.path.basename(file_path) for file_path in file_paths]


def create_v4_images_listfile(
    search_dirpath=V4_DIR, filespec="*.png", output_filepath=V4_LISTFILE_PATH
):
    file_names = get_v4_imagefile_names(search_dirpath, filespec)
    with open(output_filepath, "w") as f_out:
        for file_name in sorted(file_names):
            f_out.write("{}\n".format(file_name))


if __name__ == "__main__":
    create_v4_images_listfile()
