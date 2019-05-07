#!/usr/bin/env python

import glob
import os
import unittest

from PIL import Image
import imagehash


_HASH_SIZE = 16


class TestHash(unittest.TestCase):
    def test(self):
        self.maxDiff = None
        exceptions = []
        for fname in glob.glob("images/v4/*.png"):
            phash = imagehash.phash(Image.open(fname), hash_size=_HASH_SIZE)
            fname_base = os.path.basename(fname)
            fname_hash = os.path.splitext(fname_base)[0]
            if str(phash) != fname_hash:
                msg = 'Calculated phash {} does not match filename {!r}.'
                exceptions.append(ValueError(msg.format(str(phash), fname_base)))
        self.assertEqual([], exceptions)


class TestListing(unittest.TestCase):
    def test(self):
        # Check that the image listing file contents are up to date.
        import recreate_v4_files_listing as v4list
        file_names = set(v4list.get_v4_imagefile_names())
        listing_filepath = v4list.V4_LISTFILE_NAME
        self.assertTrue(os.path.exists(listing_filepath))
        with open(listing_filepath) as listing_file:
            listed_names = [line.strip()
                            for line in listing_file.readlines()]

        files = set(file_names)
        listed = set(listed_names)
        if listed != files:
            msg = ('Filenames in the listing file {} do not match the image '
                   'file contents of the {} directory:')
            msg = msg.format(v4list.V4_LISTFILE_NAME, v4list.V4_DIR)
            newfiles = files - listed
            if newfiles:
                msg += '\n  Names in directory, but not in the listing file:'
                msg += ''.join(['\n      ' + name for name in newfiles])
            missing = listed - files
            if missing:
                msg += '\n  Names in the listing, but not in the directory:'
                msg += ''.join(['\n      ' + name for name in missing])
            msg += ('\n\n*** Please run "{}.py" to correct. ***'.format(
                os.path.basename(v4list.__name__)))
            self.assertEqual(listed, files, msg)


if __name__ == '__main__':
    unittest.main()
