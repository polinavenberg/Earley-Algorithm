from typing import Dict, List


class CFGrammar:
    start_letter = 'S'
    rules: Dict[str, List[str]] = dict()

    def __init__(self):
        self.rules = dict()

    def add_rule(self, start: str, finish: str):
        if start in self.rules:
            self.rules[start].append(finish)
        else:
            self.rules[start] = [finish]


class Configuration:
    start: str = 'S'
    finish: str = ''
    i: int = 0

    def __init__(self, start: str, finish: str, i: int):
        self.start = start
        self.finish = finish
        self.i = i

    def __eq__(self, other):
        return self.start == other.start and self.finish == other.finish and self.i == other.i

    def __hash__(self):
        return hash(str(hash(self.start)) + str(hash(self.finish)) + str(hash(self.i)))
