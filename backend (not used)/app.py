from flask import Flask, Response, render_template, render_template_string, request, make_response, g
import json
from dialogflow_v2 import AgentsClient
app = Flask(__name__)
client = AgentsClient()
parent = client.project_path('[PROJECT]')
@app.route('/')
def index():
    response = {"payload":None}
    return make_response(json.dumps(response, sort_keys=True), 200)

@app.route('/get_chat')
def get_response():
    pass
