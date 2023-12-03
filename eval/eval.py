"""
    Uses AutoEvals to run evals
    https://github.com/braintrustdata/autoevals
"""
from autoevals.llm import *

# Create a new LLM-based evaluator
evaluator = Factuality()


class Eval:
    def __init__(self, input, output, expected) -> None:
        self.INPUT = input
        self.OUTPUT = output
        self.EXPECTED = expected

    def run_eval(self):
        result = evaluator(self.OUTPUT,
                           self.EXPECTED,
                           self.INPUT)
        return result
        

