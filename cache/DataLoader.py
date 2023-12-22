import sys, os, random
import numpy as np
import pandas as pd
import random

class DataLoader(object):
    def __init__(self):
        self.requests = []
        self.operations = []

    def get_requests(self):
        pass
    def get_operations(self):
        pass

class DataLoaderZipf(DataLoader):
    def __init__(self, num_files, num_samples, param, num_progs=1, operation='random'):
        super(DataLoaderZipf, self).__init__()

        for i in range(num_progs):
            files = np.arange(num_files)
            # Random ranks. Note that it starts from 1.
            ranks = np.random.permutation(files) + 1
            # Distribution
            pdf = 1 / np.power(ranks, param)
            pdf /= np.sum(pdf)
            # Draw samples
            self.requests += np.random.choice(files, size=num_samples, p=pdf).tolist()
            if operation == 'random':
                self.operations += np.random.choice([0, 1], size=num_samples).tolist()
            else:
                self.operations += np.full(num_samples, int(operation)).tolist()

    def get_requests(self):
        return self.requests

    def get_operations(self):
        return self.operations

class DataLoaderZipfMixed(DataLoader):
    def __init__(self, num_files, num_samples, param, num_progs=1, operation='random'):
        super(DataLoaderZipfMixed, self).__init__()

        for i in range(num_progs):
            beta = random.choice(param)
            files = np.arange(num_files)
            # Random ranks. Note that it starts from 1.
            ranks = np.random.permutation(files) + 1
            # Distribution
            pdf = 1 / np.power(ranks, beta)
            pdf /= np.sum(pdf)
            # Draw samples
            self.requests += np.random.choice(files, size=num_samples, p=pdf).tolist()
            if operation == 'random':
                self.operations += np.random.choice([0, 1], size=num_samples).tolist()
            else:
                self.operations += np.full(num_samples, int(operation)).tolist()

    def get_requests(self):
        return self.requests

    def get_operations(self):
        return self.operations