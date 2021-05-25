import re

class IterateCountry:
    def __init__(self, data):
        self.data = data
        self.href = 'https://en.wikipedia.org/wiki/'

    def __iter__(self):
        self.countries = iter(self.data)
        return self

    def __next__(self):
        country = re.sub(r'(\s)', r'_', next(self.countries)['name']['common'])
        href = self.href + country
        return [country, href]
