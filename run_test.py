#!/usr/bin/env python

from pathlib import Path

import imagehash
from PIL import Image

_HASH_SIZE = 16


class TestHash:
    def test(self):
        self.maxDiff = None
        exceptions = []
        for fname in Path("images/v4").glob("*.png"):
            phash = imagehash.phash(Image.open(fname), hash_size=_HASH_SIZE)
            fname_base = fname.name
            fname_hash = fname.stem
            if str(phash) != fname_hash:
                msg = "Calculated phash {} does not match filename {!r}."
                exceptions.append(ValueError(msg.format(str(phash), fname_base)))
        assert exceptions == [], "\n".join(str(e) for e in exceptions)


class TestListing:
    def test(self):
        # Check that the image listing file contents are up to date.
        import recreate_v4_files_listing as v4list

        file_names = set(v4list.get_v4_imagefile_names())
        listing_filepath = Path(v4list.V4_LISTFILE_NAME)
        assert listing_filepath.exists()
        with listing_filepath.open() as listing_file:
            listed_names = [line.strip() for line in listing_file.readlines()]

        files = set(file_names)
        listed = set(listed_names)
        if listed != files:
            msg = (
                "Filenames in the listing file {} do not match the image "
                "file contents of the {} directory:"
            )
            msg = msg.format(v4list.V4_LISTFILE_NAME, v4list.V4_DIR)
            newfiles = files - listed
            if newfiles:
                msg += "\n  Names in directory, but not in the listing file:"
                msg += "".join(["\n      " + name for name in newfiles])
            missing = listed - files
            if missing:
                msg += "\n  Names in the listing, but not in the directory:"
                msg += "".join(["\n      " + name for name in missing])
            msg += f'\n\n*** Please run "{Path(v4list.__file__).name}" to correct. ***'
            assert listed == files, msg
