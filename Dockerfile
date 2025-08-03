FROM ubuntu:20.04

RUN apt-get update && apt-get install -y \
    curl unzip git sudo jq\
    python3 python3-pip\
    && apt-get clean \

RUN useradd -m runner
WORKDIR /home/runner

ARG RUNNER_VERSION=2.316.0
RUN curl -L -o actions-runner-linux-x64.tar.gz https://github.com/actions/runner/releases/download/v${RUNNER_VERSION}/actions-runner-linux-x64-${RUNNER_VERSION}.tar.gz \
    && tar xzf actions-runner-linux-x64-${RUNNER_VERSION}.tar.gz \
    && rm actions-runner-linux-x64-${RUNNER_VERSION}.tar.gz

COPY entrypoint.sh /entrypoint.sh
RUN chmod +x /entrypoint.sh

# Set ownership
RUN chown -R runner:runner /home/runner

USER runner
ENTRYPOINT ["/entrypoint.sh"]