from shipping import *


class Itinerary:

    @classmethod
    def from_locations(cls, *locations):
        return cls(locations)

    def __init__(self, locations):
        self._locations = list(locations)

    def __str__(self):
        return "\n".join(location.name for location in self._locations)

    @property
    def locations(self):
        return tuple(self._locations)

    @property
    def origin(self):
        return self._locations[0]
