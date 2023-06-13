from dataclasses import dataclass

"""
create dataclass `Engine`
"""


@dataclass
class Engine:

    def __init__(self, pistons, volume):
        self.pistons = pistons
        self.volume = volume
