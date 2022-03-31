from backend.attack_repo import SharkAttackRepo
from flask import Flask, jsonify

application = Flask(__name__)


@application.route("/attacks/all", methods=['GET'])
def getAll():
    json = []
    repo = SharkAttackRepo(':memory:')
    repo.addAllCsv('/var/app/current/backend/attacks-processed-sample.csv')
    for attack in repo.getAll():
        json.append(attack.serialize())
    return jsonify(json)
