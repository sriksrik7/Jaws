from backend.attack import SharkAttack
from backend.attack_repo import SharkAttackRepo


class SharkAttackService:
    """
    Enables the retrieval of shark data
    """

    def __init__(self, repo: SharkAttackRepo):
        self.repo = repo
        self.resultCache = {}

    def get_all(self) -> [SharkAttack]:
        return self.repo.getAll()

    def get_attacks_by_address(self, address: str) -> SharkAttack:
        if address:
            if address in self.resultCache:
                return self.resultCache[address]
            result = self.repo.getByAddress(address)
            if result:
                firstResult = result[0]
                self.protect_cache_size()
                self.resultCache[address] = firstResult
                return firstResult
        return None

    def get_attacks_by_location(self, latitude: float, longitude: float, mile_radius: int) -> [SharkAttack]:
        results = []
        if latitude and longitude:
            if not mile_radius:
                mile_radius = 50
            cacheKey = toCacheKey(latitude, longitude, mile_radius)
            if cacheKey in self.resultCache:
                return self.resultCache[cacheKey]
            for attack in self.repo.getAll():
                if attack.isWithinRadius(latitude, longitude, mile_radius):
                    results.append(attack)
            self.protect_cache_size()
            self.resultCache[cacheKey] = results
        return results

    # A lazy way to protect our cloud memory
    def protect_cache_size(self):
        if len(self.resultCache) > 20:
            print('clearing cache')
            self.resultCache.clear()


def toCacheKey(latitude, longitude, mile_radius):
    return "{0}{1}{2}".format(latitude, longitude, mile_radius)
