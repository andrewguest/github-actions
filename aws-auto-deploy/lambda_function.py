# This Lambda function will return a very basic
#   JSON response


"""
In AWS Lambda, the 'event' is what contains any query parameters sent to
    the function.
    
So if you sent:
{
    "firstName": "Jason",
    "lastName": "Bourne"
}
these would be located in "event" as:

event: {
    "firstName": "Jason",
    "lastName": "Bourne"
}
"""


def lambda_handler(event, context):
    return {
        "statusCode": 200,
        "body": "Hello, this was auto deployed from Github",
        "Data that you sent": event,
    }
