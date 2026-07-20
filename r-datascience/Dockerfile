FROM rocker/r-ver:4.4

LABEL net.fairagro.sciwin.lang="r"
LABEL net.fairagro.sciwin.version="4.4"
LABEL net.fairagro.use-case="datascience"

RUN apt-get update && apt-get install -y --no-install-recommends \
    libcurl4-openssl-dev libssl-dev libxml2-dev && \
    rm -rf /var/lib/apt/lists/*
RUN R -e 'install.packages(c("tidyverse", "optparse", "jsonlite", "data.table"))'