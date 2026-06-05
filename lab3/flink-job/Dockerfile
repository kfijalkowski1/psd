FROM flink:1.20.0-scala_2.12-java17

USER root

RUN apt-get update \
    && apt-get install -y --no-install-recommends curl ca-certificates \
    && rm -rf /var/lib/apt/lists/*

RUN curl -LsSf https://astral.sh/uv/install.sh | sh
ENV PATH="/root/.local/bin:${PATH}"

WORKDIR /opt/flink/jobs

COPY pyproject.toml /opt/flink/jobs/pyproject.toml
RUN uv sync --no-dev

COPY job.py /opt/flink/jobs/job.py

RUN curl -L -o /opt/flink/lib/flink-sql-connector-kafka-3.3.0-1.20.jar \
    https://repo1.maven.org/maven2/org/apache/flink/flink-sql-connector-kafka/3.3.0-1.20/flink-sql-connector-kafka-3.3.0-1.20.jar

ENV PYTHONPATH="/opt/flink/jobs/.venv/lib/python3.11/site-packages:${PYTHONPATH}"

USER flink
