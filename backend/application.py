from backend.attack import SharkAttack
from backend.attack_repo import SharkAttackRepo
from flask import Flask, jsonify, request

application = Flask(__name__)
repo = SharkAttackRepo(':memory:')
repo.addAllCsv('/var/app/current/backend/attacks-processed.csv')
resultCache = {}


@application.route("/attacks/all", methods=['GET'])
def getAll():
    return toJson(repo.getAll())


@application.route("/attacks", methods=['GET'])
def getByLocation():
    address = request.args.get('address')
    if address:
        if address in resultCache:
            return resultCache[address]
        getByAddressResults = repo.getByAddress(address)
        if getByAddressResults:
            json = jsonify(getByAddressResults[0].serialize())
            protectCacheSize()
            resultCache[address] = json
            return json

    latitude = float(request.args.get('latitude'))
    longitude = float(request.args.get('longitude'))
    results = []
    if latitude and longitude:
        mileRadius = int(request.args.get('mileRadius'))
        if not mileRadius:
            mileRadius = 50
        cacheKey = toCacheKey(latitude, longitude, mileRadius)
        if cacheKey in resultCache:
            return resultCache[cacheKey]
        for attack in repo.getAll():
            if attack.isWithinRadius(latitude, longitude, mileRadius):
                results.append(attack)
    json = toJson(results)
    protectCacheSize()
    resultCache[cacheKey] = json
    return json


def toCacheKey(latitude, longitude, mileRadius):
    return "{0}{1}{2}".format(latitude, longitude, mileRadius)


# A lazy way to protect our cloud memory
def protectCacheSize():
    if len(resultCache) > 20:
        print('clearing cache')
        resultCache.clear()


def toJson(attacks: [SharkAttack]):
    json = []
    for attack in attacks:
        json.append(attack.serialize())
    return jsonify(json)
