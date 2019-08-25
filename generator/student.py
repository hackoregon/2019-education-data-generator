from .constants import YEAR_START_NORMS, YEAR_GROWTH_NORMS
import numpy as np


class Grade:
    """Represents the scores for one grade for a single Student."""

    def __init__(self, grade):
        self.grade = grade
        self.english = None
        self.math = None
        self.reading = None
        self.science = None

    def set_score(self, subject, score):
        if subject == 'english':
            self.english = score
        elif subject == 'math':
            self.math = score
        elif subject == 'reading':
            self.reading = score
        elif subject == 'science':
            self.science = score

    def get_score(self, subject):
        if subject == 'english':
            return self.english
        elif subject == 'math':
            return self.math
        elif subject == 'reading':
            return self.reading
        elif subject == 'science':
            return self.science
        else:
            return None

    def pretty_print(self):
        none_str = '         .  '
        if self.grade == 0:
            label = 'K'
        else:
            label = str(self.grade)
        grade_str = '\t{:>8s}'.format(label)
        for sub in ['english', 'math', 'reading', 'science']:
            if self.get_score(sub) is None:
                grade_str += none_str
            else:
                grade_str += '{:>12.2f}'.format(self.get_score(sub))
        print(grade_str)


class Student:
    """
    Represents a student in Oregon.
    Created from a passed set of demographics.
    Generates its own student data from a set of normal distributions,
    its demographics, and a strategy to generate performance scale
    factors from that information that modify the distribution.
    """

    # Constants
    RIT_START = 2004  # First year Oregon tracked RIT scores (a guess, but verify)
    THIS_YEAR = 2019

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
        scores = []
        subjects = ['english', 'math', 'reading', 'science']
        for i in range(12):  # K-11: No scores for 12th grade
            year = self.year_k + i
            if not (Student.RIT_START <= year < Student.THIS_YEAR):
                continue
            grade = Grade(i)
            for sub in subjects:
                # if the subject is measured that grade
                if sub in YEAR_START_NORMS[i].keys():
                    # if the subject was measured last grade, estimate change and add
                    # also, 11th grade has no growth norms, so default to start for now
                    # TODO: come up with a better plan than this.
                    if len(scores) > 0 and i < 11 and scores[-1].get_score(sub) is not None:
                        params = YEAR_GROWTH_NORMS[i][sub]
                        delta = np.random.normal(params['mu'], params['sigma']) + params['diff']
                        grade.set_score(sub, scores[-1].get_score(sub) + delta)
                    # otherwise, estimate a new starting grade
                    else:
                        params = YEAR_START_NORMS[i][sub]
                        grade.set_score(sub, np.random.normal(params['mu'], params['sigma']))
            scores.append(grade)
        return scores

    def pretty_print(self):
        sid = self.id_num
        gen = self.gender
        yr = self.year_k
        race = self._describe_race()
        ell = str(self.ell)[0]
        pov = str(self.poverty)[0]
        dis = str(self.disabled)[0]
        print(f"Student #{sid} ({gen}, {race}): Started {yr}, ell = {ell}, pov = {pov}, dis = {dis}")
        print("\tGrades:")
        print('\t{:>8s}{:>12s}{:>12s}{:>12s}{:>12s}'.format('GRADE', 'ENGLISH', 'MATH', 'READING', 'SCIENCE'))
        for grade in self.rit:
            grade.pretty_print()
        
    def _describe_race(self):
        if self.race == 0:
            race = 'white'
        elif self.race == 1:
            race = 'black'
        elif self.race == 2:
            race = 'hisp'
        elif self.race == 3:
            race = 'asian'
        elif self.race == 4:
            race = 'pacis'
        elif self.race == 5:
            race = 'natam'
        elif self.race == 6:
            race = 'multi'
        else:
            race = 'buggy'
        return race

    def print_to_file(self, filewriter):
        demo = [self.id_num, self.gender, self.year_k, self._describe_race(), self.ell, self.poverty, self.disabled] 
        filewriter.writerow(demo + self.rit)
