# Shared template for every use-case image. Build per folder with
# `docker build -f Dockerfile <folder>`; the folder supplies environment.yml
# and the CI workflow asserts the net.fairagro.* labels from it.
FROM mambaorg/micromamba:2.9.0

COPY --chown=$MAMBA_USER:$MAMBA_USER environment.yml /tmp/environment.yml
RUN micromamba install -y -n base -f /tmp/environment.yml && \
    micromamba clean --all --yes
