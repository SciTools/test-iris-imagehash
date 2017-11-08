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
        for fname in glob.glob("images/*.png"):
            phash = imagehash.phash(Image.open(fname), hash_size=_HASH_SIZE)
            fname_base = os.path.basename(fname)
            fname_hash = os.path.splitext(fname_base)[0]
            if str(phash) != fname_hash:
                msg = 'Calculated phash {} does not match filename {!r}.'
                exceptions.append(ValueError(msg.format(str(phash), fname_base)))
        self.assertEqual([], exceptions)


if __name__ == '__main__':
    unittest.main()
