from .student import Student
import numpy as np


class Factory:
    """This class produces fake data using the student class contained
    in this module. The constructor takes a number to be used as the size
    of the student population. The constructor also takes a distribution to
    be used for applying demographics characteristics of the students across
    the generated population. TODO: determine the type of the output to be generated."""

    def __init__(self, count, demographic_distribution, strategy):
        """
        Student Params
        :param id_num: The ID number of the student (proxy for SSN, int)
        :param year_k: The year the student started kindergarten
        :param gender: The gender of the student, "m" or "f" for now (string)
        :param race: A code for the student's race (int)
        :param ell: English language learner (boolean)
        :param poverty: Whether the student receives free/reduced lunches (boolean)
        :param disabled: Whether the student has any disabilities (boolean)
        :param strategy: How to use the above features to scale RIT scores (Strategy)
        """
        self.count = count
        self.demo = demographic_distribution
        self.strategy = strategy
        self.student_population = []
        years = list(range(2000, 2015))
        for i in range(count):
            if np.random.uniform() < self.demo['gender']:
                gender = 'f'
            else:
                gender = 'm'
            race_rand = np.random.uniform(0, sum(self.demo['race']['distribution']))
            race_code = 0
            cum_sum = 0
            for race_prop in self.demo['race']['distribution']:
                cum_sum += race_prop
                if race_rand < cum_sum:
                    break
                race_code += 1
            self.student_population.append(Student(
                id_num=i,
                year_k=np.random.choice(years),
                gender=gender,
                race=race_code,
                ell=np.random.uniform() < self.demo['race']['ell'][race_code],
                poverty=np.random.uniform() < self.demo['race']['poverty'][race_code],
                disabled=np.random.uniform() < self.demo['race']['disability'][race_code],
                strategy=self.strategy
            ))

    def pretty_print(self, head=None):
        if head is None:
            head = len(self.student_population)
        for person in self.student_population[:head]:
            person.print()

    def print_demos(self):
        men = 0
        women = 0
        races = [0, 0, 0, 0, 0, 0, 0]
        pov = 0
        ell = 0
        dis = 0
        for stud in self.student_population:
            if stud.gender == 'm':
                men += 1
            else:
                women += 1
            races[stud.race] += 1
            if stud.poverty:
                pov += 1
            if stud.ell:
                ell += 1
            if stud.disabled:
                dis += 1
        print("Generated student demographics")
        print(f"Student count: {len(self.student_population)}")
        print(f"Gender breakdown: Men = {men}, Women = {women}")
        print(f"Racial breakdown: white = {races[0]}, black = {races[1]}, hisp = {races[2]}, asian = {races[3]}")
        print(f"                  islander = {races[4]}, native Am = {races[5]}, multi = {races[6]}")
        print(f"Poverty count: {pov}")
        print(f"English learner count: {ell}")
        print(f"Disabled student count: {dis}")
