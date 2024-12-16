from flask import Flask, Response
import random
import string

app = Flask(__name__)

def generate_coupon_code():
    # Generate coupon code in the format "XXX-0000-x0x0"
    part1 = ''.join(random.choices(string.ascii_uppercase, k=3))
    part2 = ''.join(random.choices(string.digits, k=4))
    part3 = ''.join(random.choice(string.ascii_lowercase + string.digits) for _ in range(4))
    return f"{part1}-{part2}-{part3}"

@app.route('/generate-coupon', methods=['GET'])
def get_coupon():
    coupon_code = generate_coupon_code()
    # Return plain text response
    return Response(coupon_code, mimetype='text/plain')

if __name__ == '__main__':
    app.run(host='0.0.0.0', port=5000)
