from backend.attack import SharkAttack
from backend.attack_repo import SharkAttackRepo
from flask import Flask, jsonify, request

application = Flask(__name__)
repo = SharkAttackRepo(':memory:')
repo.addAllCsv('/var/app/current/backend/attacks-processed.csv')

@application.route("/attacks/all", methods=['GET'])
def getAll():
    return toJson(repo.getAll())


@application.route("/attacks", methods=['GET'])
def getByLocation():
    address = request.args.get('address')
    if address:
        getByAddressResults = repo.getByAddress(address)
        if getByAddressResults:
            return jsonify(getByAddressResults[0].serialize())

    results = []
    latitude = float(request.args.get('latitude'))
    longitude = float(request.args.get('longitude'))
    if latitude and longitude:
        mileRadius = int(request.args.get('mileRadius'))
        if not mileRadius:
            mileRadius = 50
        for attack in repo.getAll():
            if attack.isWithinRadius(latitude, longitude, mileRadius):
                results.append(attack)
    return toJson(results)


def toJson(attacks: [SharkAttack]):
    json = []
    for attack in attacks:
        json.append(attack.serialize())
    return jsonify(json)
