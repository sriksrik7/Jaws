from backend.attack import SharkAttack


def get_analytics(attacks: [SharkAttack]) -> {}:
    results = {}
    age_counter = Counter()
    male_victim_counter = BooleanCounter()
    fatality_counter = BooleanCounter()
    injury_counter = WordCounter()
    address_counter = WordCounter()
    for attack in attacks:
        age_counter.add(attack.age)
        if attack.sex:
            male_victim_counter.add('M' is attack.sex)
        if attack.fatal:
            fatality_counter.add('Y' is attack.fatal)
        if attack.injury:
            injury_counter.add(attack.injury)
        if attack.address:
            address_counter.add(attack.address)

    results['averageAge'] = age_counter.get_average()
    results['fatalityPercentage'] = fatality_counter.get_percentage(True)
    results['survivalPercentage'] = fatality_counter.get_percentage(False)
    results['femaleVictimPercentage'] = male_victim_counter.get_percentage(False)
    results['maleVictimPercentage'] = male_victim_counter.get_percentage(True)
    results['mostCommonInjury'] = injury_counter.get_most_common()
    results['mostCommonLocation'] = address_counter.get_most_common()
    results['resultCount'] = len(attacks)
    return results


class WordCounter():
    def __init__(self):
        self.counts = {}

    def add(self, values: str):
        for value in values.split(', '):
            if value in self.counts:
                count = self.counts[value] + 1
            else:
                count = 1
            self.counts[value] = count

    def get_most_common(self):
        print(self.counts)
        return max(self.counts, key=self.counts.get)


class Counter:
    def __init__(self):
        self.sum = 0
        self.count = 0

    def add(self, value: str):
        if value:
            try:
                intVal = int(value)
                self.sum = self.sum + intVal
                self.count = self.count + 1
            except Exception:
                return

    def get_average(self):
        return self.sum / self.count


class BooleanCounter:
    def __init__(self):
        self.trueCount = 0
        self.falseCount = 0
        self.resultCount = 0

    def add(self, value):
        if value:
            self.trueCount = self.trueCount + 1
        else:
            self.falseCount = self.falseCount + 1
        self.resultCount = self.resultCount + 1

    def get_percentage(self, value: bool):
        if value:
            percentage = (self.trueCount / self.resultCount) * 100
        else:
            percentage = (self.falseCount / self.resultCount) * 100
        return str(round(percentage, 2)) + '%'
