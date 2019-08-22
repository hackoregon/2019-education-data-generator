import numpy as np


class Strategy:
    """
    How to choose proficiency scale factors for a student.
    This base strategy simply returns the computed factor for each subject,
    But can also be considered to define the interface for more complex
    strategies that inherit from it.
    """
    def _compute_generic_factor(self, student):
        """
        Defines the strategy for computing a general proficiency scale factor
        for a student with given demographics.
        :param student: A Student object
        :return: A float multiplier.
        """
        return 1.0

    def _compute_english_factor(self, student):
        """
        Defines the strategy for computing an English proficiency scale factor
        for a student with given demographics.
        :param student: A Student object
        :return: A float multiplier.
        """
        return 1.0

    def _compute_math_factor(self, student):
        """
        Defines the strategy for computing a math proficiency scale factor
        for a student with given demographics.
        :param student: A Student object
        :return: A float multiplier.
        """
        return 1.0

    def _compute_reading_factor(self, student):
        """
        Defines the strategy for computing a reading proficiency scale factor
        for a student with given demographics.
        :param student: A Student object
        :return: A float multiplier.
        """
        return 1.0

    def _compute_science_factor(self, student):
        """
        Defines the strategy for computing a science proficiency scale factor
        for a student with given demographics.
        :param student: A Student object
        :return: A float multiplier.
        """
        return 1.0

    def get_proficiency_factors(self, student):
        """
        Use the demographics of the Student object to compute proficiency scale factors.
        This is the only function that should be called by the Student, and shouldn't change.
        The individual computations should themselves change.
        :param student: A Student object
        :return: A dictionary of scale factors
        """
        gen_apt = self._compute_generic_factor(student)
        return {
            "english": gen_apt * self._compute_english_factor(student),
            "math": gen_apt * self._compute_math_factor(student),
            "reading": gen_apt * self._compute_reading_factor(student),
            "science": gen_apt * self._compute_science_factor(student)
        }


class NoDemoStrategy(Strategy):
    """
    This strategy assumes that no student demographics have any correlation with performance,
    but that individual students show a particular propensity for some subjects and a
    general one for learning in general.
    """

    def _compute_generic_factor(self, student):
        """
        The generic proficiency of a student gives a bonus or penalty to every subject.
        :param student: A Student object
        :return: A float multiplier.
        """
        mu = 1
        sigma = 0.05
        return np.random.normal(mu, sigma)

    def _compute_english_factor(self, student):
        """
        The English proficiency of a student gives a bonus or penalty to every subject.
        :param student: A Student object
        :return: A float multiplier.
        """
        mu = 1
        sigma = 0.05
        return np.random.normal(mu, sigma)

    def _compute_math_factor(self, student):
        """
        The Math proficiency of a student gives a bonus or penalty to every subject.
        :param student: A Student object
        :return: A float multiplier.
        """
        mu = 1
        sigma = 0.05
        return np.random.normal(mu, sigma)

    def _compute_reading_factor(self, student):
        """
        The reading proficiency of a student gives a bonus or penalty to every subject.
        :param student: A Student object
        :return: A float multiplier.
        """
        mu = 1
        sigma = 0.05
        return np.random.normal(mu, sigma)

    def _compute_science_factor(self, student):
        """
        The Science proficiency of a student gives a bonus or penalty to every subject.
        :param student: A Student object
        :return: A float multiplier.
        """
        mu = 1
        sigma = 0.05
        return np.random.normal(mu, sigma)


class DemoStrategy(Strategy):
    """
    """

    def __init__(self, pov_cost, ell_cost, dis_cost):
        self.pov_cost = pov_cost
        self.ell_cost = ell_cost
        self.dis_cost = dis_cost

    def _compute_generic_factor(self, student):
        """
        The generic proficiency of a student gives a bonus or penalty to every subject.
        :param student: A Student object
        :return: A float multiplier.
        """
        mu = 1 - student.poverty * self.pov_cost
        sigma = 0.05
        return np.random.normal(mu, sigma)

    def _compute_english_factor(self, student):
        """
        The English proficiency of a student gives a bonus or penalty to every subject.
        :param student: A Student object
        :return: A float multiplier.
        """
        mu = 1 - student.ell * self.ell_cost + student.disabled * np.random.uniform(-1, 1) * self.dis_cost
        sigma = 0.05
        return np.random.normal(mu, sigma)

    def _compute_math_factor(self, student):
        """
        The Math proficiency of a student gives a bonus or penalty to every subject.
        :param student: A Student object
        :return: A float multiplier.
        """
        mu = 1 + student.disabled * np.random.uniform(-1, 1) * self.dis_cost
        sigma = 0.05
        return np.random.normal(mu, sigma)

    def _compute_reading_factor(self, student):
        """
        The reading proficiency of a student gives a bonus or penalty to every subject.
        :param student: A Student object
        :return: A float multiplier.
        """
        mu = 1 - student.ell * self.ell_cost + student.disabled * np.random.uniform(-1, 1) * self.dis_cost
        sigma = 0.05
        return np.random.normal(mu, sigma)

    def _compute_science_factor(self, student):
        """
        The Science proficiency of a student gives a bonus or penalty to every subject.
        :param student: A Student object
        :return: A float multiplier.
        """
        mu = 1 + student.disabled * np.random.uniform(-1, 1) * self.dis_cost
        sigma = 0.05
        return np.random.normal(mu, sigma)

