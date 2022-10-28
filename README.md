# Python IoT Temperature Sensor Mock

A Python function to mock 100 IoT sensors that read environment temperature.

The function sometimes returns `nan` instead of a temperature float to simulate sensor failures.

Tested with **Python 3.9** but should also work seamlessly with newer versions.

## Helpful links

There is a plug-and-play library for Python software to connect to **Google PubSub** which is used:

- [google-cloud-pubsub Library](https://github.com/googleapis/python-pubsub)

Also, here's a **quickstart** on how to deploy Google Cloud Functions written in Python:

- [Docs - Google Cloud Functions](https://cloud.google.com/functions/docs/create-deploy-http-python)

The example mock function uses a **framework for rapid development** of serverless functions in Python called `functions-framework`:

- [functions-framework-python](https://github.com/GoogleCloudPlatform/functions-framework-python)
