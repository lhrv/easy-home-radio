import os
from flask import Flask
app = Flask(__name__)

@app.route('/start')
def start_fip():
    print('starting fip...')
    os.system('mpv https://stream.radiofrance.fr/fip/fip_hifi.m3u8 &')
    return 'fip started'

@app.route('/stop')
def stop_fip():
    print('stopping fip...')
    os.system('pkill mpv')
    return 'fip stopped'

@app.route('/')
def hello_world():
    return 'Hello, World!'

if __name__ == "__main__":
    app.run(host='0.0.0.0', port=8080, debug=True)
