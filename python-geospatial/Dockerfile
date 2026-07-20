FROM python:3.13-slim

RUN apt-get update && apt-get install -y --no-install-recommends \
    gdal-bin libgdal-dev && rm -rf /var/lib/apt/lists/*

LABEL net.fairagro.sciwin.lang="python"
LABEL net.fairagro.sciwin.version="3.13"
LABEL net.fairagro.use-case="datascience"

RUN pip install --no-cache-dir \
    pandas==3.0.4 \
    contextily==1.7.0 \
    geopandas==1.1.4 \
    matplotlib==3.10.6 \
    geopy==2.4.1\
    networkx==3.6.1 \
    osmnx==2.1.0 \
    shapely==2.1.2