from sys import getrecursionlimit, setrecursionlimit
getrecursionlimit()
import timeit

class RecursiveTemplate:

    def __init__(self):
        pass

    def recursion(self, iterate: int, condition: int, params: int):
        """
        1. recursive terminator
        """
        if iterate > condition:
            """
            4. process result logic in last steps
            """
            self.process_last_result(...)
            return
        """
        2. process current level logic(base case)
        """
        self.process_level(iterate, ...)
        """
        3. process next level logic(recursion relationship)
        """
        self.recursion(iterate + 1, ...)

        """
        5.(optional) reverse current level states 
        """
        self.reverse_status()

        """
        6.(optional) return results
        """

    def process_last_result(self):
        pass

    def process_level(self, level, param):
        pass

    def reverse_status(self):
        pass
