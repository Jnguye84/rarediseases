from flask import Flask, request, Response
import requests
from flask_cors import CORS  # Import CORS

app = Flask(__name__)
CORS(app)  # Enable CORS on the Flask app
NEO4J_URL = "http://localhost:7474/browser"  # Default URL where Neo4j browser is running

@app.route('/', defaults={'path': ''}, methods=["GET", "POST", "PUT", "DELETE", "PATCH"])
@app.route('/<path:path>', methods=["GET", "POST", "PUT", "DELETE", "PATCH"])
def proxy(path):
    global NEO4J_URL
    if request.method == "GET":
        resp = requests.get(f'{NEO4J_URL}/{path}', stream=True)
    elif request.method == "POST":
        resp = requests.post(f'{NEO4J_URL}/{path}', json=request.json, stream=True)
    elif request.method == "PUT":
        resp = requests.put(f'{NEO4J_URL}/{path}', json=request.json, stream=True)
    elif request.method == "DELETE":
        resp = requests.delete(f'{NEO4J_URL}/{path}', stream=True)
    elif request.method == "PATCH":
        resp = requests.patch(f'{NEO4J_URL}/{path}', json=request.json, stream=True)
    else:
        return 'Unsupported HTTP method', 405

    excluded_headers = ['content-encoding', 'content-length', 'transfer-encoding', 'connection']
    headers = [(name, value) for (name, value) in resp.raw.headers.items()
               if name.lower() not in excluded_headers]
    response = Response(resp.content, resp.status_code, headers)
    return response

if __name__ == '__main__':
    app.run(port=8888, debug=True)
