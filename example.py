
from pyflowchart import Flowchart
import pygraphviz as pgv
import graphviz2drawio
import drawpyo


def calculate(a, b):
    if a > b:
        return a - b
    else:
        for i in range(3):
            print(f"循环{i}")
        return a + b

result = calculate(5, 3)
print(result)