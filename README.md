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

## Acknowledgements

- Thanks to the Google Cloud Platform teams for providing the [`functions-framework`](https://github.com/GoogleCloudPlatform/functions-framework-python) as well as the [Python Google PubSub library](https://github.com/googleapis/python-pubsub).

## Authors

- [@torbendury](https://www.github.com/torbendury)

## Contributing

Contributions are always welcome!

If you find any bugs or security issues, open a GitHub issue and describe it. Anyone is very welcome to contribute to and enhance this project, so feel free to open a PR for your issue.

## Deployment

To deploy this project run

```bash
  gcloud functions deploy iot-mock \
    --entry-point=entrypoint \
    --runtime=python39 \
    --allow-unauthenticated \
    --gen2 \
    --trigger-http \
    --memory=128MB \
    --source=src/ \
    --set-env-vars=GOOGLE_PUBSUB_TOPIC=${my-topic},GOOGLE_CLOUD_PROJECT=${my-project}
```

This will deploy a GCF `iot-mock` into your configured project. It runs on Python 3.9 and is *public to the internet*.
It is triggered via a HTTP(S) endpoint and gets 128MB of reserved RAM.

**Note:** If you want the mock data to be regularly pushed, you will want to place a **Google Cloud Scheduler** in front of it, which regularly calls the GCF endpoint.

The PubSub topic that the function is pushing data to is retrieved by the environment variable `GOOGLE_PUBSUB_TOPIC`. Normally, `GOOGLE_CLOUD_PROJECT` is always set to the project where your function is running, but in case your function needs to be deployed into a different project than your PubSub topic resides in, you can override it with the deployment command above.

If you need further help deploying a Google Cloud Function, refer to the [official documentation](https://cloud.google.com/functions/docs/create-deploy-http-python).

## Features

- Send JSON (random) temperature data to a PubSub topic
- Send `'nan'` (as a valid Python float) on a random basis
- Include an ISO 8601 compliant timestamp to the data point
- Sensor IDs from 0 to 99

## Feedback

If you have any feedback, please reach out to me via GitHub issues.

## License

This repository is published unter the [Apache 2.0](LICENSE) license.

Read on more about it [here](https://choosealicense.com/licenses/apache-2.0/).
