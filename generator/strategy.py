import math

from .constants import DIS_PCT, ELL_PCT, POV_PCT
import numpy as np


class Strategy:
    """
    How to choose proficiency scale factors for a student.
    This base strategy simply returns the computed factor for each subject,
    But can also be considered to define the interface for more complex
    strategies that inherit from it.
    """

    def __init__(self):
        # These are used in more complex Strategies
        self.generic_mu = 0
        self.generic_sigma = math.sqrt(50)
        self.english_mu = 0
        self.english_sigma = math.sqrt(50)
        self.math_mu = 0
        self.math_sigma = math.sqrt(50)
        self.reading_mu = 0
        self.reading_sigma = math.sqrt(50)
        self.science_mu = 0
        self.science_sigma = math.sqrt(50)

    def _compute_generic_factor(self, student):
        """
        Defines the strategy for computing a general proficiency scale factor
        for a student with given demographics.
        :param student: A Student object
        :return: A float multiplier.
        """
        return 0.0

    def _compute_english_factor(self, student):
        """
        Defines the strategy for computing an English proficiency scale factor
        for a student with given demographics.
        :param student: A Student object
        :return: A float multiplier.
        """
        return 0.0

    def _compute_math_factor(self, student):
        """
        Defines the strategy for computing a math proficiency scale factor
        for a student with given demographics.
        :param student: A Student object
        :return: A float multiplier.
        """
        return 0.0

    def _compute_reading_factor(self, student):
        """
        Defines the strategy for computing a reading proficiency scale factor
        for a student with given demographics.
        :param student: A Student object
        :return: A float multiplier.
        """
        return 0.0

    def _compute_science_factor(self, student):
        """
        Defines the strategy for computing a science proficiency scale factor
        for a student with given demographics.
        :param student: A Student object
        :return: A float multiplier.
        """
        return 0.0

    def get_proficiency_bonuses(self, student):
        """
        Use the demographics of the Student object to compute proficiency scale factors.
        This is the only function that should be called by the Student, and shouldn't change.
        The individual computations should themselves change.
        :param student: A Student object
        :return: A dictionary of scale factors
        """
        gen_apt = self._compute_generic_factor(student)
        return {
            "english": gen_apt + self._compute_english_factor(student),
            "math": gen_apt + self._compute_math_factor(student),
            "reading": gen_apt + self._compute_reading_factor(student),
            "science": gen_apt + self._compute_science_factor(student)
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
        return np.random.normal(self.generic_mu, self.generic_sigma)

    def _compute_english_factor(self, student):
        """
        The English proficiency of a student gives a bonus or penalty to every subject.
        :param student: A Student object
        :return: A float multiplier.
        """
        return np.random.normal(self.english_mu, self.english_sigma)

    def _compute_math_factor(self, student):
        """
        The Math proficiency of a student gives a bonus or penalty to every subject.
        :param student: A Student object
        :return: A float multiplier.
        """
        return np.random.normal(self.math_mu, self.math_sigma)

    def _compute_reading_factor(self, student):
        """
        The reading proficiency of a student gives a bonus or penalty to every subject.
        :param student: A Student object
        :return: A float multiplier.
        """
        return np.random.normal(self.reading_mu, self.reading_sigma)

    def _compute_science_factor(self, student):
        """
        The Science proficiency of a student gives a bonus or penalty to every subject.
        :param student: A Student object
        :return: A float multiplier.
        """
        return np.random.normal(self.science_mu, self.science_sigma)


class DemoStrategy(Strategy):
    """
    """

    def __init__(self, dis_size, ell_sigma, ell_cost, pov_sigma, pov_cost):
        super().__init__()
        self.dis_size = dis_size
        self.desired_ell_sigma = ell_sigma
        self.ell_cost = ell_cost
        self.ell_posi = self._compute_positive_ell_effect()
        self.desired_pov_sigma = pov_sigma
        self.pov_cost = pov_cost
        self.pov_posi = self._compute_positive_poverty_effect()

    def _compute_positive_ell_effect(self):
        """
        When we presume the negative effect of a demographic and the desired variation
        of a distribution in which one class gets a uniform negative effect and the other
        a uniform positive one, and where we want to keep the mean effect at 0, we can
        compute the necessary positive effect to line things up.

        :return: a real number representing the positive effect
        """
        if self.desired_ell_sigma**2 - self.ell_cost**2 * ELL_PCT < 0:
            raise ValueError("Negative ell effect is too large compared to the desired variance.")
        return math.sqrt((self.desired_ell_sigma**2 - self.ell_cost**2 * ELL_PCT)/(1 - ELL_PCT))

    def _compute_positive_poverty_effect(self):
        """
        When we presume the negative effect of a demographic and the desired variation
        of a distribution in which one class gets a uniform negative effect and the other
        a uniform positive one, and where we want to keep the mean effect at 0, we can
        compute the necessary positive effect to line things up.

        :return: a real number representing the positive effect
        """
        if self.desired_pov_sigma**2 - self.pov_cost**2 * POV_PCT < 0:
            raise ValueError("Negative poverty effect is too large compared to the desired variance.")
        return math.sqrt((self.desired_pov_sigma**2 - self.pov_cost**2 * POV_PCT)/(1 - POV_PCT))

    def _compute_generic_factor(self, student):
        """
        The generic proficiency of a student gives a bonus or penalty to every subject.
        :param student: a Student object
        :return: a float bonus
        """
        if student.poverty:
            mu = self.pov_cost
        else:
            mu = self.pov_posi
        sigma = math.sqrt(50 - self.desired_pov_sigma**2)
        return np.random.normal(mu, sigma)

    def _compute_english_factor(self, student):
        """
        The English proficiency of a student gives a bonus or penalty to English RIT scores.
        :param student: a Student object
        :return: a float multiplier
        """
        if student.ell:
            mu = self.ell_cost
        else:
            mu = self.ell_posi
        mu += student.disabled * np.random.uniform(-1, 1) * self.dis_size
        sigma = math.sqrt(50 - self.desired_ell_sigma**2 - 25*(DIS_PCT**2))
        return np.random.normal(mu, sigma)

    def _compute_math_factor(self, student):
        """
        The Math proficiency of a student gives a bonus or penalty to math RIT scores.
        :param student: A Student object
        :return: a float multiplier
        """
        mu = student.disabled * np.random.uniform(-1, 1) * self.dis_size
        sigma = math.sqrt(50 - 25*(DIS_PCT**2))
        return np.random.normal(mu, sigma)

    def _compute_reading_factor(self, student):
        """
        The reading proficiency of a student gives a bonus or penalty to reading RIT scores.
        :param student: A Student object
        :return: a float multiplier
        """
        if student.ell:
            mu = self.ell_cost
        else:
            mu = self.ell_posi
        mu += student.disabled * np.random.uniform(-1, 1) * self.dis_size
        sigma = math.sqrt(50 - self.desired_ell_sigma**2 - 25*(DIS_PCT**2))
        return np.random.normal(mu, sigma)

    def _compute_science_factor(self, student):
        """
        The Science proficiency of a student gives a bonus or penalty to science RIT scores.
        :param student: A Student object
        :return: a float multiplier
        """
        mu = student.disabled * np.random.uniform(-1, 1) * self.dis_size
        sigma = math.sqrt(50 - 25*(DIS_PCT**2))
        return np.random.normal(mu, sigma)
