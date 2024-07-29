from flask import jsonify, request, Blueprint, json


router = Blueprint("app_router", __name__)

@router.route('/', methods = ['GET'])
def home():
    if(request.method == 'GET'):
        data = "hello to my simple app"
        return jsonify({'message': data})


@router.route('/sum', methods = ['GET', 'POST'])
def sum():
    """
    Function to sum two numbers, works through GET and POST methods. Numbers
    given by the user must by passed in variables `num1` and `num2`.

    Parameters
    ----------
        GET: get two numbers through query parameters.
             Example: curl -X GET "http://127.0.0.1:5000/sum?num1=1&num2=2"
        POST: get two numbers through a json file.
              Example: curl -X POST -H "Content-type: application/json" -d "{\"num1\" : 1, \"num2\" : 2}" "localhost:5000/sum"
    Returns
    -------
        JSON response with the result
    """
    # TODO: Check if request method is GET or POST
    # TODO: In case you get a GET request, obtain num1 and num2 values from
    #       the request, then assign them variables num1 and num1.
    # TODO: In case you get a POST request, first check the user sent the data
    #       through JSON, i.e. 'Content-Type' == 'application/json'.
    #       Then, load the JSON data and get num1 and num2 values,
    #       assign them variables num1 and num1.
    num1 = None
    num2 = None

    # This code should run as a it is
    result = num1 + num2
    return jsonify({'result': result})