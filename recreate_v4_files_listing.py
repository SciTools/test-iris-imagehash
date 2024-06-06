#!/usr/bin/env python

"""Regenerate v4_files_listing.txt ."""

from __future__ import annotations

from pathlib import Path

REPO_MAIN_DIRPATH = Path(__file__).resolve().parent
V4_DIR = REPO_MAIN_DIRPATH / "images" / "v4"
V4_LISTFILE_NAME = "v4_files_listing.txt"
V4_LISTFILE_PATH = REPO_MAIN_DIRPATH / V4_LISTFILE_NAME


def get_v4_imagefile_names(
    search_dirpath: Path = V4_DIR,
    filespec: str = "*.png",
) -> list[str]:
    """Return a list of the current image files in the v4 subdirectory."""
    file_paths = search_dirpath.glob(filespec)
    return [file_path.name for file_path in file_paths]


def create_v4_images_listfile(
    search_dirpath: Path = V4_DIR,
    filespec: str = "*.png",
    output_filepath: Path = V4_LISTFILE_PATH,
) -> None:
    """Create a listfile of the current image files in the v4 subdirectory."""
    file_names = get_v4_imagefile_names(search_dirpath, filespec)
    with output_filepath.open("w") as f_out:
        for file_name in sorted(file_names):
            f_out.write(f"{file_name}\n")


if __name__ == "__main__":
    create_v4_images_listfile()
