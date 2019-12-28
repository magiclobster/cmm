FROM python:3-slim-stretch

ENV DEBIAN_FRONTEND noninteractive
ARG APT_FLAGS_COMMON="-qq -y --no-install-recommends"

RUN apt-get update && apt-get install ${APT_FLAGS_COMMON} \
    procps
