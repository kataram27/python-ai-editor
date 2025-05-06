from flask import Flask, request, jsonify
from flask_cors import CORS  # ✅ Add this
import io
import contextlib
import numpy as np
import pandas as pd

app = Flask(__name__)
CORS(app)  # ✅ Allow all origins by default

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
    app.run(debug=True)
