from flask import Flask, request, jsonify
from cipher.caesar import CaesarCipher  
from cipher.vigenere import VigenereCipher

app = Flask(__name__)

#CAESAR CIPHER ALGORITHM
caesar_cipher = CaesarCipher()  

@app.route("/api/caesar/encrypt", methods=["POST"])
def caesar_encrypt():
    try:
        data = request.get_json()
        if not data or "plain_text" not in data or "key" not in data:
            return jsonify({"error": "Thiếu dữ liệu đầu vào"}), 400

        plain_text = data["plain_text"]
        key = int(data["key"])

        encrypted_text = caesar_cipher.encrypt_text(plain_text, key)
        return jsonify({"encrypted_message": encrypted_text})

    except ValueError:
        return jsonify({"error": "Key phải là số nguyên"}), 400
    except Exception as e:
        return jsonify({"error": f"Lỗi hệ thống: {str(e)}"}), 500

@app.route("/api/caesar/decrypt", methods=["POST"])
def caesar_decrypt():
    try:
        data = request.get_json()
        if not data or "cipher_text" not in data or "key" not in data:
            return jsonify({"error": "Thiếu dữ liệu đầu vào"}), 400

        cipher_text = data["cipher_text"]
        key = int(data["key"])

        decrypted_text = caesar_cipher.decrypt_text(cipher_text, key)
        return jsonify({"decrypted_message": decrypted_text})

    except ValueError:
        return jsonify({"error": "Key phải là số nguyên"}), 400
    except Exception as e:
        return jsonify({"error": f"Lỗi hệ thống: {str(e)}"}), 500


#VIGENERE CIPHER ALGORITHM
vigenere_cipher = VigenereCipher()

@app.route('/api/vigenere/encrypt', methods=['POST'])
def vigenere_encrypt():
    data = request.json 
    plain_text = data['plain_text']
    key = data['key']
    encrypted_text = vigenere_cipher.vigenere_encrypt(plain_text, key)
    return jsonify({'encrypted_text':encrypted_text})

@app.route('/api/vigenere/decrypt', methods=['POST'])
def vigenere_decrypt():
    data = request.json 
    cipher_text = data['cipher_text']
    key = data['key']
    decrypted_text = vigenere_cipher.vigenere_decrypt(cipher_text, key)
    return jsonify({'decrypted_text': decrypted_text})
if __name__ == "__main__":
    app.run(host="0.0.0.0", port=5000, debug=True)  
