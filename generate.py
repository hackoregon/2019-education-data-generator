# A simple script to generate a set of students
import math

from generator.factory import Factory
from generator.strategy import DemoStrategy
from generator.constants import DEMO, ELL_PCT, POV_PCT
import numpy as np

# Choices
n = 100000  # Number of students desired
dis_size = math.sqrt(300)/2  # max possible mean change for a student with a disability
ell_sigma = math.sqrt(10)    # desired standard deviation of effect of being an English learner
# drop for english learners in reading and english
ell_cost = math.sqrt(ell_sigma**2/(ELL_PCT**2 - ELL_PCT**3 + ELL_PCT))
pov_sigma = math.sqrt(10)    # desired standard deviation of effect of poverty
# drop for students in poverty in general aptitude
pov_cost = math.sqrt(pov_sigma**2/(POV_PCT**2 - POV_PCT**3 + POV_PCT))

strat = DemoStrategy(dis_size, ell_sigma, ell_cost, pov_sigma, pov_cost)
stud_fact = Factory(n, DEMO, strat)
stud_fact.print_demos()

# inspect a few students
does = np.random.choice(stud_fact.student_population, 10, replace=False)

print("\nA Student Sample")
for doe in does:
    doe.pretty_print()
