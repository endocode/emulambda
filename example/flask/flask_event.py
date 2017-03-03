from flask import Flask

app = Flask(__name__)

@app.route('/', methods=['GET', 'POST'])
def lambda_handler(event=None, context=None):
    print "Lambda function invoked /"
    response = LambdaResponse()

    return {
        'statusCode': response.status,
        'headers': response.response_headers,
        'body': "ok"
    }

class LambdaResponse(object):
    def __init__(self):
        self.status = None
        self.response_headers = None

    def start_response(self, status, response_headers, exc_info=None):
        self.status = int(status[:3])
        self.response_headers = dict(response_headers)

if __name__ == '__main__':
    app.run(debug=True)
