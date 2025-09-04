from flask import Flask, request, jsonify, send_file, send_from_directory
import qrcode
import io
import time
import json
import os
from cryptography.fernet import Fernet

# Flask app
app = Flask(__name__, static_folder="static")

# Directory to save QR codes
SAVE_DIR = r"F:\mini project\code\saved_qr_codes"
os.makedirs(SAVE_DIR, exist_ok=True)


@app.route("/")
def home():
    return send_from_directory(app.static_folder, "index.html")


# Generate QR image
def make_qr(data, filename=None):
    qr = qrcode.QRCode(version=1, box_size=10, border=5)
    qr.add_data(data)
    qr.make(fit=True)
    img = qr.make_image(fill="black", back_color="white")

    # Save to disk if filename provided
    if filename:
        filepath = os.path.join(SAVE_DIR, filename)
        img.save(filepath)

    # Also return as in-memory file
    buf = io.BytesIO()
    img.save(buf, format="PNG")
    buf.seek(0)
    return buf


@app.route('/encrypt', methods=['POST'])
def encrypt():
    try:
        text = request.form.get('text')
        expiry = request.form.get('expiry')
        passphrase = request.form.get('passphrase')

        if not text or not expiry or not passphrase:
            return jsonify({"error": "Missing input fields"}), 400

        expiry = int(expiry)
        expiry_time = int(time.time()) + expiry

        # Generate encryption key + encrypt text
        key = Fernet.generate_key()
        cipher = Fernet(key)
        encrypted = cipher.encrypt(text.encode())

        # Save cipher details to file
        with open("secret.json", "w") as f:
            json.dump({
                "cipher": encrypted.decode(),
                "expiry": expiry_time,
                "duration": expiry,
                "key": key.decode()
            }, f)

        # Generate unique QR filename
        filename = f"qr_{int(time.time())}.png"

        # Create + save QR to disk and buffer
        buf = make_qr(encrypted.decode(), filename)

        # Return QR image as response
        return send_file(buf, mimetype="image/png")

    except Exception as e:
        return jsonify({"error": f"Encryption failed: {str(e)}"}), 500


@app.route('/decrypt', methods=['POST'])
def decrypt():
    try:
        file = request.files['qrfile']
        passphrase = request.form.get('passphrase')

        # Load cipher details
        with open("secret.json") as f:
            secret = json.load(f)

        expiry_time = secret["expiry"]
        duration = secret["duration"]  # original user-set duration

        if time.time() > expiry_time:
            return jsonify({"error": "Message expired"})

        # Decrypt text
        cipher = Fernet(secret["key"].encode())
        decrypted = cipher.decrypt(secret["cipher"].encode()).decode()

        # Return decrypted message + original expiry duration
        return jsonify({
            "message": decrypted,
            "expiry": duration
        })

    except Exception as e:
        return jsonify({"error": f"Decryption failed: {str(e)}"}), 500


if __name__ == "__main__":
    app.run(debug=True)
