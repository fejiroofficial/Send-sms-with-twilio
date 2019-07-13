# Send-sms-with-twilio
Simple script for sending an sms with Twilio, Flask and Ngrok.


## Running the application
To run this application, clone the repository on your local machine and execute the following command.
```sh
    $ cd send-sms-with-twilio
    $ virtualenv venv
    $ source venv/bin/activate
    $ pip install -r requirements.txt
    $ python send_sms.py (to receive an sms)
    $ python run.py (to reply an sms)
    $ cd into folder where ngrok is downloaded and run ./ngrok http 5000
    $ Send a message to twilio number and await reply
```

Create an account with twilio [`here`](https://www.twilio.com/)

