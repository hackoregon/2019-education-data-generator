# A simple script to generate a set of students

from generator.factory import Factory
from generator.strategy import NoDemoStrategy
from generator.constants import DEMO
import numpy as np

# Choices
n = 100000  # Number of students desired

strat = NoDemoStrategy()
stud_fact = Factory(n, DEMO, strat)
stud_fact.print_demos()

# inspect a few students
does = np.random.choice(stud_fact.student_population, 10, replace=False)

print("\nA Student Sample")
for doe in does:
    doe.pretty_print()
