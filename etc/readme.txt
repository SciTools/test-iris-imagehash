This file details how the perceptual image hash files were created.

Package plan for installation in environment /home/travis/miniconda/envs/test-environment:

The following packages will be downloaded:

    package                    |            build
    ---------------------------|-----------------
    jpeg-9b                    |                0         918 KB  conda-forge
    libgfortran-3.0.0          |                1         281 KB  defaults
    xz-5.2.2                   |                0         853 KB  conda-forge
    libpng-1.6.24              |                0         311 KB  conda-forge
    libtiff-4.0.6              |                6         507 KB  conda-forge
    openblas-0.2.18            |                5        14.1 MB  conda-forge
    blas-1.1                   |         openblas           1 KB  conda-forge
    freetype-2.6.3             |                1         2.8 MB  conda-forge
    numpy-1.11.2               |py27_blas_openblas_200         7.1 MB  conda-forge
    pillow-3.4.1               |           py27_1         925 KB  conda-forge
    pywavelets-0.4.0           |      np111py27_0         1.7 MB  conda-forge
    scipy-0.18.1               |np111py27_blas_openblas_200        32.3 MB  conda-forge
    ------------------------------------------------------------
                                           Total:        61.7 MB

The imagerepo.json file (and associated phash files) were created with the
imagehash.phash function, using a hash_size=16, a tolerance=2, and the above
software stack. 

A phash image is considered not similar to the list of registered expected phash
images for an individual test case iff it has a phash hamming distance greater
than the specified tolerance for *all* of the registered expected phash images. 

Note that, the calculation of a phash for an image *may* be sensitive to the
version of pillow. The use of pillow 3.3.1 and at least 3.4.0 showed a minor
difference in the calculation of 12 phash images.
