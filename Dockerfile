FROM ghcr.io/prefix-dev/pixi:0.78.0 AS build

WORKDIR /build
COPY pixi.toml pixi.lock ./
RUN pixi install --locked -e default

FROM debian:trixie-slim
COPY --from=build /build/.pixi/envs/default /opt/env
RUN useradd --create-home --uid 1000 sciwin

ENV PATH="/opt/env/bin:$PATH" \
    CONDA_PREFIX="/opt/env" \
    GDAL_DATA="/opt/env/share/gdal" \
    PROJ_DATA="/opt/env/share/proj" \
    GDAL_DRIVER_PATH="/opt/env/lib/gdalplugins"

USER sciwin

ENTRYPOINT []