from backend.attack_repo import SharkAttackRepo
from flask import Flask, jsonify

app = Flask(__name__)


@app.route("/attacks/all")
def getAll():
    json = []
    repo = SharkAttackRepo(':memory:')
    repo.addAllCsv('/var/app/current/backend/attacks-processed-sample.csv')
    for attack in repo.getAll():
        json.append(attack.serialize())
    return jsonify(json)
