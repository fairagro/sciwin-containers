# Shared template for every use-case image. Build per folder with
# `docker build -f Dockerfile <folder>`; the folder supplies environment.yml
# and the CI workflow asserts the net.fairagro.* labels from it.
FROM mambaorg/micromamba:2.9.0

COPY --chown=$MAMBA_USER:$MAMBA_USER environment.yml /tmp/environment.yml
RUN micromamba install -y -n base -f /tmp/environment.yml && \
    micromamba clean --all --force-pkgs-dirs --yes && \
    find /opt/conda -follow -type f -name '*.a' -delete && \
    find /opt/conda -follow -type f -name '*.pyc' -delete && \
    find /opt/conda -follow -type d -name '__pycache__' -exec rm -rf '{}' + && \
    rm -rf /opt/conda/share/doc /opt/conda/share/man /opt/conda/share/info
