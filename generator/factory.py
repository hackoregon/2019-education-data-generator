from generator.student import Student
from generator.strategy import Strategy
import random

#sample distribution
test_distribution = {
    "year_k": 0,
    "gender": 0,
    "race": 0,
    "ell": 0,
    "poverty": 0,
    "disabled": 0,
}

class Factory:
    """This class produces fake data using the student class contained
    in this module. The constructor takes a number to be used as the size
    of the student population. The constructor also takes a distribution to 
    be used for applying demographics characteristics of the students across
    the generated population. TODO: determine the type of the output to be generated."""

    def __init__(self, count, demographic_distribution):
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
        self.demographic_distribution = demographic_distribution
        #TODO: Use the demographic_distribution to create the students
        self.student_population = []
        years = list(range(2000, 2015))
        genders = ["m", "f"]
        races = [1,2,3,4,5]
        for i in range(count):
            year = random.choice(years)
            self.student_population.append(Student(i, random.choice(years) ,random.choice(genders), random.choice(races), False, False, False, Strategy()))
            

    def pretty_print(self):
        for person in self.student_population:
            print(person.year_k)
