from backend.attack import SharkAttack
from backend.attack_analytics import get_analytics
from backend.attack_repo import SharkAttackRepo
from backend.attack_service import SharkAttackService
from flask import Flask, jsonify, request

application = Flask(__name__)
repo = SharkAttackRepo(':memory:')
repo.addAllCsv('attacks-processed.csv')
service = SharkAttackService(repo)


@application.route("/attacks/all", methods=['GET'])
def getAll():
    return toJson(service.get_all())


@application.route("/attacks", methods=['GET'])
def getByLocation():
    address = request.args.get('address')
    if address:
        return jsonify(service.get_attacks_by_address(address).serialize())
    latitude = float(request.args.get('latitude'))
    longitude = float(request.args.get('longitude'))
    if latitude and longitude:
        mileRadius = int(request.args.get('mileRadius'))
        return toJson(service.get_attacks_by_location(latitude, longitude, mileRadius))
    return jsonify([])


@application.route("/attacks/analytics", methods=['GET'])
def getAnalytics():
    latitude = float(request.args.get('latitude'))
    longitude = float(request.args.get('longitude'))
    if latitude and longitude:
        mileRadius = int(request.args.get('mileRadius'))
        attacks = service.get_attacks_by_location(latitude, longitude, mileRadius)
        return jsonify(get_analytics(attacks))
    return jsonify({})


def toJson(attacks: [SharkAttack]):
    json = []
    for attack in attacks:
        json.append(attack.serialize())
    return jsonify(json)
