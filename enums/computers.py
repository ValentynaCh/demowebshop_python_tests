from enum import Enum


class Computers(Enum):
    desktops = 'Desktops',
    notebooks = 'Notebooks'
    accessories = 'Accessories'

    @classmethod
    def list(cls):
        return list(map(lambda c: c.value, cls))
