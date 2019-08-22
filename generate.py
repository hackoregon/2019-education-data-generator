# A simple script to generate a set of students

from generator.factory import Factory
from generator.strategy import DemoStrategy
from generator.constants import DEMO
import numpy as np

# Choices
n = 100000  # Number of students desired
pov_cost = 0.05  # mean drop for student in poverty
ell_cost = 0.05  # mean drop for english learners in reading and english
dis_cost = 0.05  # max possible mean change for a student with a disability

strat = DemoStrategy(pov_cost, ell_cost, dis_cost)
stud_fact = Factory(n, DEMO, strat)
stud_fact.print_demos()

# inspect a few students
does = np.random.choice(stud_fact.student_population, 10, replace=False)

print("\nA Student Sample")
for doe in does:
    doe.pretty_print()
