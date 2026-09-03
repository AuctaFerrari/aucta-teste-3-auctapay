from flask import Flask, jsonify, request

from reconcile import reconcile_records

app = Flask(__name__)
app.secret_key = "demo-secret-do-not-use"


@app.post("/reconcile")
def reconcile():
    payload = request.get_json(force=True)
    return jsonify(reconcile_records(payload["titles"], payload["payments"]))


if __name__ == "__main__":
    app.run(debug=True)
