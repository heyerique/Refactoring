from counter import Counter


class GenderCounter:

    _male_counter = None
    _female_counter = None

    def __init__(self):
        self._male_counter = Counter()
        self._male_counter.name = 'Male'

        self._female_counter = Counter()
        self._female_counter.name = 'Female'

    @property
    def male_count(self):
        return self._male_counter.count

    @male_count.setter
    def male_count(self, count):
        self._male_counter.count = count

    @property
    def female_count(self):
        return self._female_counter.count

    @female_count.setter
    def female_count(self, count):
        self._female_counter.count = count

    @property
    def total_count(self):
        return self._male_counter.count + self._female_counter.count

    @property
    def formatted_data(self):
        return {self._male_counter.name: self._male_counter.count,
                self._female_counter.name: self._female_counter.count}