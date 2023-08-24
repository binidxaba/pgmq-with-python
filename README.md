# Using pgmq with Python

This repository contains a couple of scripts to demonstrate how to use pgmq with Python.

## Running the scripts

Start a pgmq docker container:

```console
docker run -d --name postgres -e POSTGRES_PASSWORD=postgres -p 5432:5432 quay.io/tembo/pgmq-pg:latest
```

Install the pgmq library with pip:

```console
pip install tembo-pgmq-python
```

Run the scripts:

```console
sh ./run_test.sh
```
