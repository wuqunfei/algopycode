from typing import Dict


class RM:

    def __init__(self):
        # init cache
        self.cache: Dict = {}

    def recursive(self, arg):
        # Base case
        if arg is False:
            return

        # Get from cache
        if arg in self.cache:
            return self.cache.get(arg)
        # Recursion case
        result = self.recursive(arg - 1)
        # Write into cache
        self.cache[arg] = result
        return result
