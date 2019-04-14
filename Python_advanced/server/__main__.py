import json
import yaml
import socket
import argparse
from setting import (
    ENCODING, HOST, PORT, BUFFERSIZE
)

encoding = ENCODING
host = HOST
port = PORT
buffersize = BUFFERSIZE

parser = argparse.ArgumentParser()
parser.add_argument(
    '-c', '--config', type=str,
    help='Sets run configuration'
)

args = parser.parse_args()

if args.config:
    with open(args.config) as file:
        conf = yaml.load(file, Loader=yaml.Loader)
        host = conf.get('host', host)
        port = conf.get('port', port)
        buffersize = conf.get('buffersize', buffersize)

try:
    sock = socket.socket()
    sock.bind((host, port))
    sock.listen(5)

    print('Server started')

    while True:
        client, address = sock.accept()
        print(
            'Client with address {} was detected'.format(address)
        )
        bdata = client.recv(buffersize)
        request = json.loads(bdata.decode(encoding))
        response = json.dumps(request)
        client.send(response.encode(encoding))
        
        client.close()
except KeyboardInterrupt:
    print('Server closed')

