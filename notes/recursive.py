
class RecursiveTemplate:
    def __init__(self):
        self.boundary_condition = 100

    def recursion(self, level: int, params: int):
        """
        1. recursive terminator
        """
        if level > self.boundary_condition:
            """
            4. process latest level logic
            """
            self.process_last_result(...)
            return
        """
        2. process current level logic
        """
        self.process_level(level, ...)
        """
        3. process next level logic in recursion
        """
        self.recursion(level + 1, ...)

        """
        5.(optional) reverse current level states 
        """
        self.reverse_status()

    def process_last_result(self):
        pass

    def process_level(self, level, param):
        pass

    def reverse_status(self):
        pass
