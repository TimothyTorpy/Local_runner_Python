FROM ubuntu:20.04

ENV DEBIAN_FRONTEND=noninteractive

RUN apt-get update && apt-get install -y \
    curl unzip git sudo jq\
    python3 python3-pip\
    libicu66 \
    libssl1.1 \
    libkrb5-3 \
    zlib1g \
    libcurl4 \
    && apt-get clean 

RUN useradd -m runner
WORKDIR /home/runner

ARG RUNNER_VERSION=2.316.0
ENV RUNNER_VERSION=${RUNNER_VERSION}
RUN curl -L -o actions-runner-linux-x64.tar.gz https://github.com/actions/runner/releases/download/v${RUNNER_VERSION}/actions-runner-linux-x64-${RUNNER_VERSION}.tar.gz \
    && tar xzf actions-runner-linux-x64.tar.gz \
    && rm actions-runner-linux-x64.tar.gz

COPY entrypoint.sh /entrypoint.sh
RUN chmod +x /entrypoint.sh

# Set ownership
RUN chown -R runner:runner /home/runner

USER runner
ENTRYPOINT ["/entrypoint.sh"]