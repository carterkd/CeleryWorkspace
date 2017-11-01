# CeleryWorkspace
The module created by following the instructions at http://docs.celeryproject.org/en/latest/getting-started/first-steps-with-celery.html#application

To use this module, you'll first need to install RabbitMQ (`sudo apt-get install rabbitmq` or `brew install rabbitmq`) and then celery (`pip install celery`).

To run the module, navigate to the `CeleryModule` folder, and run `celery -A tasks worker --loglevel=info`. Then, in a separate terminal window, run `python taskCaller.py`, and you should see the message passed between the two windows.
