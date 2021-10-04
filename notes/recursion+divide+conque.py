from typing import List, Optional
from functools import reduce


class DivideConquer:

    def divide_conquer(self, problem, parameters):
        """
        1. recursion terminator
        """
        if problem is None:
            return
        """
        2. divide problem into sub problems with data
        """
        dataset: List = self.divide_data(problem)
        problems: List = self.divde_problem(problem, dataset)
        """
        3. apply and conquer sub problems
        """
        solutions: List = list(map(self.divide_conquer, problems, [parameters] * len(problem)))
        """
        4. combine and merge all the solutions into result
        """
        rev = reduce(self.combine, solutions)
        return rev

    def divde_problem(self, problem, dataset):
        return []

    def combine(self, solutions):
        return

    def divide_data(self, problem):
        return []
