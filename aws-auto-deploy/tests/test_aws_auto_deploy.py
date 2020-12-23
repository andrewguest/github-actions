from lambda_function import lambda_handler


def test_lambda_handler():
    testDict = {"firstValue": 100, "secondValue": "second"}

    # call the "lambda_handler" function that we're testing, pass it our
    #   "testDict" to simulate query parameters and save the returned value(s) to "result"
    result = lambda_handler(testDict, "myContext")

    # check that it returns a "dict" type
    assert type(result) is dict

    # check that the "statusCode" key has a value of 200
    assert result["statusCode"] == 200

    assert result["body"] == "Hello, this was auto deployed from Github"

    # check that the 'Data that you sent' key returned contains the correct
    #   values for each of our keys that we sent it
    assert result["Data that you sent"]["firstValue"] == 100
    assert result["Data that you sent"]["secondValue"] == "second"
