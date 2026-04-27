#!/usr/bin/env python
# TextAugment: mixup
#
# Copyright (C) 2018-2023
# Authors: Joseph Sefara, Vukosi Marivate
#
# URL: <https://github.com/dsfsi/textaugment/>
# For license information, see LICENSE
import numpy as np
import random


class MIXUP:
    """
    This class implements the mixup algorithm [1] for natural language processing.

    [1] Zhang, Hongyi, Moustapha Cisse, Yann N. Dauphin, and David Lopez-Paz. "mixup: Beyond empirical risk
    minimization." in International Conference on Learning Representations (2018).
    https://openreview.net/forum?id=r1Ddp1-Rb
    """

    @staticmethod
    def validate(**kwargs):
        """Validate input data"""
        pass

    def __init__(self, random_state=1, runs=1):
        self.random_state = random_state
        self.runs = runs
        if isinstance(self.random_state, int):
            random.seed(self.random_state)
            np.random.seed(self.random_state)
        else:
            raise TypeError("random_state must have type int")

    def mixup_data(self, x, y=None, alpha=0.2):
        """This method performs mixup. If runs = 1 it just does 1 mixup with whole batch, any n of runs
        creates many mixup matches.

        :type x: Numpy array
        :param x: Data array
        :type y: Numpy array
        :param y: (optional) labels
        :type alpha: float
        :param alpha: alpha

        :rtype: tuple
        :return: Returns mixed inputs, pairs of targets, and lambda
        """
        pass

    def flow(self, data, labels=None, batch_size=32, shuffle=True, runs=1):
        """This function implements the batch iterator and specifically calls mixup

        :param data: Input data. Numpy ndarray or list of lists.
        :param labels: Labels. Numpy ndarray or list of lists.
        :param batch_size: Int (default: 32).
        :param shuffle: Boolean (default: True).
        :param runs: Int (default: 1). Number of augmentations

        :rtype:   array or tuple
        :return:  array or tuple of arrays (X_data array, labels array)."""
        pass
