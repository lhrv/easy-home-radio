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
