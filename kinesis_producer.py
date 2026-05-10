import boto3
import json
import random
import time
from datetime import datetime, timezone

STREAM_NAME = "CS178ClickStream"
REGION_NAME = "us-east-1"

kinesis = boto3.client("kinesis", region_name=REGION_NAME)

pages = ["/", "/menu", "/schedule", "/assignments", "/contact"]
users = ["student-1", "student-2", "student-3", "student-4"]

for i in range(10):
    event = {
        "event_id": i + 1,
        "event_type": "page_view",
        "user_id": random.choice(users),
        "page": random.choice(pages),
        "timestamp": datetime.now(timezone.utc).isoformat()
    }

    response = kinesis.put_record(
        StreamName=STREAM_NAME,
        Data=json.dumps(event),
        PartitionKey=event["user_id"]
    )

    print("Sent event:", event)
    print("ShardId:", response["ShardId"])
    print("SequenceNumber:", response["SequenceNumber"])
    print("-" * 50)

    time.sleep(1)
