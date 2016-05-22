import requests

from flask import Flask, request, Response
from werkzeug.datastructures import Headers

from two1.wallet import Wallet
from two1.bitserv.flask import Payment

NOMINATIM_HOST = 'ec2-52-40-116-115.us-west-2.compute.amazonaws.com'
NOMINATIM_PORT = '80'

app = Flask(__name__)

wallet = Wallet()
payment = Payment(app, wallet)

def do_call(method_name):
    url = 'http://{}:{}/nominatim/{}.php'.format(NOMINATIM_HOST, NOMINATIM_PORT, method_name)
    r = requests.get(
        url=url,
        params=request.args if request.args else None)
    resp = Response(
        r.text if r.text else None,
        status = r.status_code)
    return resp

@app.route('/reverse')
@payment.required(5)
def reverse():
    return do_call('reverse')

@app.route('/search')
@payment.required(5)
def reverse():
    return do_call('search')

if __name__ == '__main__':
    app.run(host='0.0.0.0', port=5001)
