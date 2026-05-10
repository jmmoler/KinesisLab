import boto3
import json

STREAM_NAME = "CS178ClickStream"
REGION_NAME = "us-east-1"

kinesis = boto3.client("kinesis", region_name=REGION_NAME)

stream_description = kinesis.describe_stream(StreamName=STREAM_NAME)
shard_id = stream_description["StreamDescription"]["Shards"][0]["ShardId"]

shard_iterator_response = kinesis.get_shard_iterator(
    StreamName=STREAM_NAME,
    ShardId=shard_id,
    ShardIteratorType="TRIM_HORIZON"
)

shard_iterator = shard_iterator_response["ShardIterator"]

print(f"Reading records from stream: {STREAM_NAME}")
print(f"Using shard: {shard_id}")
print("-" * 50)

records_response = kinesis.get_records(
    ShardIterator=shard_iterator,
    Limit=20
)

records = records_response["Records"]

if not records:
    print("No records found yet. Run the producer first, then try again.")
else:
    for record in records:
        data = json.loads(record["Data"].decode("utf-8"))
        print("Received record:")
        print(json.dumps(data, indent=2))
        print("PartitionKey:", record["PartitionKey"])
        print("SequenceNumber:", record["SequenceNumber"])
        print("-" * 50)
