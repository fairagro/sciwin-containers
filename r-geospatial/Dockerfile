FROM rocker/geospatial:4.4

LABEL net.fairagro.sciwin.lang="r"
LABEL net.fairagro.sciwin.version="4.4"
LABEL net.fairagro.sciwin.requirements='[\
    "RColorBrewer", \
    "RNetCDF", \
    "classInt", \
    "deldir", \
    "gstat", \
    "hdf5r", \
    "lidR", \
    "mapdata", \
    "mapview", \
    "ncdf4", \
    "proj4", \
    "raster", \
    "rlas", \
    "sf", \
    "sfarrow", \
    "sp", \
    "spacetime", \
    "spatstat", \
    "spatialreg", \
    "spdep", \
    "stars", \
    "terra", \
    "tidync", \
    "tmap", \
    "geoR", \
    "geosphere", \
    "BiocManager",\
    "optparse" \
]'
LABEL net.fairagro.use-case="datascience"

RUN R -e 'install.packages(c("optparse"))'