from pwn import *
import json
import base64
import binascii
import codecs
import sys

def decode(t, data):
    """
    The function decodes data based on the specified encoding type.
    
    :param t: The type of encoding to be used for decoding the data. It can be one of the following:
    'base64', 'hex', 'bigint', 'rot13', or 'utf-8'
    :param data: The encoded data that needs to be decoded
    :return: The function is not returning anything, it is just defining different cases for decoding
    data based on the given type (t) and returning the decoded data in each case.
    """
    if t == 'base64':
        return base64.b64decode(data).decode('utf-8')
    elif t == 'hex':
        return binascii.unhexlify(data).decode('utf-8')
    elif t == 'bigint':
        return binascii.unhexlify(data.replace('0x', '')).decode('utf-8')
    elif t == 'rot13':
        return codecs.encode(data, 'rot_13')
    elif t == 'utf-8':
        s = ""
        for c in data:
            s += chr(c)
        return s


r = remote('socket.cryptohack.org', 13377, level = 'debug')

def json_recv():
    """
    The function `json_recv()` receives a JSON-formatted message and returns it as a Python object.
    :return: The function `json_recv()` is returning a JSON object that is decoded from a string
    received from a socket connection.
    """
    line = r.recvline()
    """
    The `json.loads(line.decode())` function call is decoding a JSON-formatted string received from a socket connection and 
    returning a Python object. The `line` variable is a byte string received from the socket connection, which is then decoded 
    using the `decode()` method to convert it to a Unicode string. The resulting Unicode string is then passed to the `json.loads()` function, 
    which parses the string and returns a Python object (e.g. a dictionary or a list) that represents the JSON data. 
    The `return` statement then returns this Python object to the caller of the `json_recv()` function.
    """
    return json.loads(line.decode())

def json_send(hsh):
    """
    The function takes a dictionary, converts it to a JSON string, encodes it, and sends it as a
    request.
    
    :param hsh: The parameter `hsh` is a dictionary (hash) that contains key-value pairs. This function
    converts the dictionary into a JSON string and sends it as a request using the `sendline` method of
    an object named `r`
    """
    request = json.dumps(hsh).encode()
    r.sendline(request)

# The code is continuously receiving JSON-formatted messages from a remote server using a socket
# connection. It then checks if the received message contains a "flag" key. If it does, it prints the
# flag and exits the program. If not, it decodes the "encoded" value in the received message using the
# specified encoding type ("type" key) and sends the decoded value back to the server in a new
# JSON-formatted message using the "json_send" function. This process continues until a flag is
# received and the program exits.
while True:

    received = json_recv()

    if "flag" in received:
        print("FLAG: %s" % received["flag"])
        sys.exit(0)

    to_send = {
        "decoded": decode(received["type"], received["encoded"])
    }
    json_send(to_send)