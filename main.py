from flask import Flask
import random
import string

app = Flask(__name__)

def generate_coupon():
    part1 = ''.join(random.choices(string.ascii_uppercase, k=3))
    part2 = ''.join(random.choices(string.digits, k=4))
    part3 = ''.join(random.choices(string.ascii_lowercase + string.digits, k=4))
    return f"{part1}-{part2}-{part3}"

@app.route('/generate-coupon', methods=['GET'])
def generate_coupon_api():
    coupon = generate_coupon()
    return coupon  # Return as plain text
