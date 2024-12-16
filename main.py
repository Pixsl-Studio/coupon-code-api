from flask import Flask, jsonify
import random
import string

app = Flask(__name__)

def generate_coupon_code():
    part1 = ''.join(random.choices(string.ascii_uppercase, k=3))  # XXX
    part2 = ''.join(random.choices(string.digits, k=4))          # 0000
    part3 = ''.join(random.choice(string.ascii_lowercase + string.digits) for _ in range(4))  # x0x0
    return f"{part1}-{part2}-{part3}"

@app.route('/generate-coupon', methods=['GET'])
def generate_coupon():
    coupon_code = generate_coupon_code()
    return jsonify({"coupon_code": coupon_code})

if __name__ == '__main__':
    app.run(host='0.0.0.0', port=5000)
