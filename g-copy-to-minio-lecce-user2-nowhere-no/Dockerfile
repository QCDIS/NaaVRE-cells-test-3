FROM ghcr.io/naavre/flavors/naavre-fl-biodt-hackathon25-cell-build:v0.0.7 AS build
COPY --chown=$MAMBA_USER:$MAMBA_USER environment.yaml .
RUN micromamba install -y -n venv -f environment.yaml
ARG MAMBA_DOCKERFILE_ACTIVATE=1
USER root
RUN conda-pack -p /opt/conda/envs/venv -o /tmp/env.tar && \
    mkdir /venv && cd /venv && tar xf /tmp/env.tar && \
    rm /tmp/env.tar
RUN /venv/bin/conda-unpack

FROM ghcr.io/naavre/flavors/naavre-fl-biodt-hackathon25-cell-runtime:v0.0.7 AS runtime
COPY --from=build /venv /venv
WORKDIR /app
COPY . .