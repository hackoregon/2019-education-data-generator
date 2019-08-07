class Strategy:
    """
    How to choose proficiency scale factors for a student.
    This base strategy simply returns the computed factor for each subject,
    But can also be considered to define the interface for more complex
    strategies that inherit from it.
    """
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
        return {
            "english": self._compute_english_factor(student),
            "math": self._compute_math_factor(student),
            "reading": self._compute_reading_factor(student),
            "science": self._compute_science_factor(student)
        }
