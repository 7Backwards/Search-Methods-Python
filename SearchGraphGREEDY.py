# Greedy Search
from SearchGraph import SearchGraph


class SearchGraphGREEDY(SearchGraph):

    def __init__(self, nameMethod, origin, destiny, countryMap, isLimited):
        super().__init__(self, nameMethod, origin, destiny, countryMap)
        self.isLimited = isLimited
