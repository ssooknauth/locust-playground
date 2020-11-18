from flask import Flask

server_port = 9999
svc = Flask(__name__)
svc.debug = True

@svc.route('/test')
def hey():
    return 'Welcome folks!'

if __name__ == "__main__":
    svc.run('0.0.0.0',port=server_port)