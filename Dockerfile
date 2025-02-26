FROM python:3.13-slim-bookworm AS builder

WORKDIR /app

RUN echo 'Acquire::http::Pipeline-Depth 0;\nAcquire::http::No-Cache true;\nAcquire::BrokenProxy true;\n' > /etc/apt/apt.conf.d/99fixbadproxy

RUN apt-get update --allow-releaseinfo-change --fix-missing

# Install build dependencies
RUN apt-get install -y build-essential 
RUN apt-get install -y curl
RUN apt-get install -y software-properties-common

ENV POETRY_HOME=/opt/poetry
ENV POETRY_NO_INTERACTION=1
ENV POETRY_VIRTUALENVS_CREATE=false
ENV PATH=/opt/poetry/bin:$PATH

# Upgrade pip and setuptools to fix security vulnerabilities
RUN pip3 install --upgrade pip setuptools

RUN pip3 install poetry

# Copy and install dependencies
COPY poetry.lock pyproject.toml /app/

# Use this if the secret is in Environment Variables
# ARG BOSCHDEVCLOUD_USERNAME
# ARG BOSCHDEVCLOUD_TOKEN
# ENV POETRY_HTTP_BASIC_MODANALIT_USERNAME=${BOSCHDEVCLOUD_USERNAME}
# ENV POETRY_HTTP_BASIC_MODANALIT_PASSWORD=${BOSCHDEVCLOUD_TOKEN}
# poetry install --no-ansi --no-root

# Use this if the secret is in Github Secrets
RUN --mount=type=secret,id=BOSCHDEVCLOUD_USERNAME \
  --mount=type=secret,id=BOSCHDEVCLOUD_TOKEN \
   export POETRY_HTTP_BASIC_MODANALIT_USERNAME=$(cat /run/secrets/BOSCHDEVCLOUD_USERNAME) && \
   export POETRY_HTTP_BASIC_MODANALIT_PASSWORD=$(cat /run/secrets/BOSCHDEVCLOUD_TOKEN) && \
   poetry install --no-ansi --no-root

FROM python:3.13-slim-bookworm AS server

WORKDIR /app

ENV POETRY_HOME=/opt/poetry \
    POETRY_NO_INTERACTION=1 \
    POETRY_VIRTUALENVS_CREATE=false
ENV PATH=/opt/poetry/bin:$PATH

# Upgrade pip and setuptools to fix security vulnerabilities
RUN pip3 install --upgrade pip setuptools

# Copy only necessary files from builder
COPY --from=builder /app /app
COPY --from=builder /usr/local/lib/python3.13 /usr/local/lib/python3.13
COPY --from=builder /usr/local/bin /usr/local/bin

ENV PATH="/app/.venv/bin:$PATH"

COPY ./ /app

RUN poetry install --no-ansi --only-root

EXPOSE 8080

# CMD ["modanalit", "run", ".\app\Home.py", "--server.port=8080", "--server.address=0.0.0.0"]
# CMD ["streamlit", "run", ".\app\Home.py", "--server.port=8080", "--server.address=0.0.0.0"]
