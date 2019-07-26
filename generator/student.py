

class Student:
    """
    Represents a student in Oregon.
    Created from a passed set of demographics.
    Generates its own student data from a set of normal distributions,
    its demographics, and a strategy to generate performance scale
    factors from that information that modify the distribution.
    """

    def __init__(self, id_num, year_k, gender, race, ell, poverty, disabled, strategy):
        """
        :param id_num: The ID number of the student (proxy for SSN, int)
        :param year_k: The year the student started kindergarten
        :param gender: The gender of the student, "m" or "f" for now (string)
        :param race: A code for the student's race (int)
        :param ell: English language learner (boolean)
        :param poverty: Whether the student receives free/reduced lunches (boolean)
        :param disabled: Whether the student has any disabilities (boolean)
        :param strategy: How to use the above features to scale RIT scores (Strategy)
        """
        self.id_num = id_num
        self.year_k = year_k
        self.gender = gender
        self.race = race
        self.ell = ell
        self.poverty = poverty
        self.disabled = disabled
        self.factors = strategy.get_proficiency_factors(student=self)
        self.rit = self.generate_scores()

    def generate_scores(self):
        """
        Generates RIT scores.
        :return: A dictionary of RIT scores for the appropriate number of years/subjects
        """
        return {}