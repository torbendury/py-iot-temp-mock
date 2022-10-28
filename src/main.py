"""
Generates a random temperature float when called via HTTP and pushes a new data point to Google
PubSub. WARNING: Intended for testing purposes. Might fail at any time. Not intended for
production usage.
"""
import json
import os
import random
from datetime import datetime
import functions_framework
from flask import Request
from google.cloud import pubsub_v1

GOOGLE_PROJECT = os.getenv("GOOGLE_CLOUD_PROJECT")
GOOGLE_PUBSUB_TOPIC = os.getenv("GOOGLE_PUBSUB_TOPIC")
CANONICAL_GOOGLE_PUBSUB_TOPIC = f"projects/{GOOGLE_PROJECT}/topics/{GOOGLE_PUBSUB_TOPIC}"


def get_temperature() -> float:
    """A utility function to generate random temperature floats or generate a simulated sensor
    failure. In case of a simulated failure, 'nan' will be returned as a valid float value.

    Returns:
        float: A random float number to mock a temperature or 'nan' so simulate sensor errors.
    """
    temperature = round(random.uniform(-40.00, 150), 2)
    if temperature * 10 % 2 == 0:
        temperature = float("nan")
    return temperature


def publish_data(data: dict) -> None:
    """Utilizes the Google Cloud PubSub library to push a dictionary of data to a PubSub topic.

    Args:
        data (dict): A valid Python dictionary containing data which will be sent.
    """
    publisher = pubsub_v1.PublisherClient()
    byte_data = json.dumps(data, indent=2).encode("utf-8")
    response = publisher.publish(topic=CANONICAL_GOOGLE_PUBSUB_TOPIC, data=byte_data)
    print(response.result())


@functions_framework.http
def entrypoint(request: Request):
    # pylint: disable=unused-argument
    """Entrypoint function for the Google Cloud Function. Utilizes the Flask framework
    as well as the Google Cloud functions-framework for Python.

    Args:
        request (Request): The incoming Flask HTTP request. Unused in this function but must be
        provided for a correct entrypoint.
    """
    publish_data(
        {
            "id": random.randint(0, 99),
            "timestamp": datetime.utcnow().replace(microsecond=0).isoformat(),
            "temperature": get_temperature(),
        }
    )
