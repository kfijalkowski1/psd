#!/usr/bin/env bash
set -euo pipefail

BOOTSTRAP_SERVER="${BOOTSTRAP_SERVER:-kafka:29092}"

echo "Creating Kafka demo topics on ${BOOTSTRAP_SERVER}..."

kafka-topics --bootstrap-server "${BOOTSTRAP_SERVER}" --create --if-not-exists --topic temperature-input --partitions 1 --replication-factor 1
kafka-topics --bootstrap-server "${BOOTSTRAP_SERVER}" --create --if-not-exists --topic temperature-below-zero --partitions 1 --replication-factor 1

echo "Topics ready:"
kafka-topics --bootstrap-server "${BOOTSTRAP_SERVER}" --list
