class RB:

    def __init__(self):
        self.output = []

    def backtrack(self, candidate, parameters):

        # Meet all the conditions
        if self.find_solution(self, candidate):
            self.output.append(candidate)
            return
        candidates = []
        for next_candidate in candidates:
            # try and place the condition
            self.try_candidate(next_candidate)
            self.backtrack(next_candidate, parameters + 1)
            self.revese_candidate(next_candidate)

    def find_solution(self, self1, candidate):
        pass

    def try_candidate(self, next_candidate):
        pass

    def revese_candidate(self, next_candidate):
        pass
