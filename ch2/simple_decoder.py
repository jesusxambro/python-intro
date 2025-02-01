import base64

def crack_base64(encoded_string):
    try:
        decoded_bytes = base64.b64decode(encoded_string)
        decoded_string = decoded_bytes.decode('utf-8')
        return decoded_string
    except Exception as e:
        print(f"Decoding error: {e}")
        return None

# encoded_message = "QXVzdGluIENvbW11bml0eSBDb2xsZWdl"
encoded_message = "fsdfgwergergergergergerg"

decoded_message = crack_base64(encoded_message)

if decoded_message:
    print(f"Decoded message: {decoded_message}")
else:
    print("Could not decode the message.")
