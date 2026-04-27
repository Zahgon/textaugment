#!/usr/bin/env python
# TextAugment: AEDA
#
# Copyright (C) 2023
# Author: Juhwan Choi
#
# URL: <https://github.com/dsfsi/textaugment/>
# For license information, see LICENSE
#
"""
This module is an implementation of the original AEDA algorithm (2021) [1].
"""
import random


class AEDA:
    """
    This class is an implementation of the original AEDA algorithm (2021) [1].

    [1] Karimi et al., 2021, November. AEDA: An Easier Data Augmentation Technique for Text Classification.
    In Findings of the Association for Computational Linguistics: EMNLP 2021 (pp. 2748-2754).
    https://aclanthology.org/2021.findings-emnlp.234.pdf

    Example usage: ::
        >>> from textaugment import AEDA
        >>> t = AEDA()
        >>> t.punct_insertion("John is going to town")
        ! John is going to town
    """

    @staticmethod
    def validate(**kwargs):
        """Validate input data"""
        pass

    def __init__(self, punctuations=['.', ';', '?', ':', '!', ','], random_state=1):
        """A method to initialize parameters

        :type punctuations: list
        :param punctuations: (optional) Punctuations to be inserted
        :type random_state: int
        :param random_state: (optional) Seed

        :rtype:   None
        :return:  Constructer do not return.
        """
        self.punctuations = punctuations
        self.random_state = random_state
        if isinstance(self.random_state, int):
            random.seed(self.random_state)
        else:
            raise TypeError("random_state must have type int")

    def punct_insertion(self, sentence: str):
        """Insert random punctuations to the sentence

        :type sentence: str
        :param sentence: Sentence

        :rtype:   str
        :return:  Augmented sentence
        """
        pass
