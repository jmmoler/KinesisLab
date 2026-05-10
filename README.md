# CS178 Kinesis Data Streams Lab

This repository supports a CS178-style AWS lab introducing Amazon Kinesis Data Streams.

## Goal

Students will:

1. Create a Kinesis Data Stream.
2. Send fake clickstream events using Python and boto3.
3. Read records back from the stream.
4. Explain producers, consumers, records, shards, and partition keys.
5. Delete the stream to avoid unwanted charges.

## Files

- `kinesis_producer.py` sends fake website click events to Kinesis.
- `kinesis_consumer.py` reads records from Kinesis.
- `requirements.txt` lists Python dependencies.
- `CS178_Kinesis_HackMD.md` contains the HackMD-ready lab writeup.

## Setup

Install dependencies:

```bash
pip3 install -r requirements.txt
```

Configure AWS credentials:

```bash
aws configure
```

Create a Kinesis stream named:

```text
CS178ClickStream
```

Then run:

```bash
python3 kinesis_producer.py
python3 kinesis_consumer.py
```

## Cleanup

Delete the `CS178ClickStream` stream after finishing the lab.
