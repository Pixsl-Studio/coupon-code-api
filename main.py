from flask import Flask, jsonify
import random
import string

app = Flask(__name__)

@app.route('/')
def generate_coupon():
    coupon = ''.join(random.choices(string.ascii_uppercase + string.digits, k=8))
    return jsonify({coupon})

if __name__ == '__main__':
    app.run(host='0.0.0.0', port=5000)
