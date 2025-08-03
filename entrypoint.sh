#!/bin/bash
set -e

# Required ENV vars: REPO_URL, RUNNER_TOKEN
if [[ -z "$REPO_URL" || -z "$RUNNER_TOKEN" ]]; then
  echo "Missing REPO_URL or RUNNER_TOKEN env variables"
  exit 1
fi

cd /home/runner

./config.sh --unattended \
  --url "${REPO_URL}" \
  --token "${RUNNER_TOKEN}" \
  --name "$(hostname)" \
  --work _work \
  --replace

trap 'echo "Removing runner..."; ./config.sh remove --unattended --token $RUNNER_TOKEN' EXIT

./run.sh