from factory.generator.student import Student
from factory.generator.strategy import Strategy

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
        """Use the demographic_distribution to create the students"""
        "def student: __init__(self, id_num, year_k, gender, race, ell, poverty, disabled, strategy):"
        self.student_population = []
        for i in range(count):
            self.student_population.append(Student(i, 2 ,"m", 3, True, False, False, Strategy()))
        """for kid in student_population:
            print(kid.id_num)"""
        