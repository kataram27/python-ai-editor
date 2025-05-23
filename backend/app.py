from flask import Flask, request, jsonify, send_from_directory
from flask_cors import CORS
import io
import contextlib
import numpy as np
import pandas as pd
import os

app = Flask(__name__, static_folder="../frontend", static_url_path="")
CORS(app)

@app.route("/")
def serve_frontend():
    return send_from_directory(app.static_folder, "index.html")

@app.route("/run", methods=["POST"])
def run_code():
    code = request.json.get("code", "")
    output = io.StringIO()

    try:
        with contextlib.redirect_stdout(output):
            exec(code, {"np": np, "pd": pd})
    except Exception as e:
        output.write(str(e))

    return jsonify({"output": output.getvalue()})

if __name__ == "__main__":
    port = int(os.environ.get("PORT", 5000))
    app.run(host="0.0.0.0", port=port, debug=True)
