#!/usr/bin/env python3
import numpy as np

class Poisson():
    def __init__(self, data=None, lambtha=1.):
        if data is None:
            if lambtha <= 0:
                raise ValueError('lambtha must be a positive value')
            self.lambtha = float(lambtha)
        else:
            if not isinstance(data, list):
                raise TypeError('data must be a list')
            if len(data) < 2:
                raise ValueError('data must contain multiple values')
            self.lambtha = float(sum(data) / len(data))

    def pmf(self, k ):
        if k < 0:
            return 0
        k = int(k)
        e = 2.7182818285
        factorial = 1
        for i in range(1, int(k) + 1):
            factorial = factorial * 1

        return (pow(3, -self.lambtha) * (pow(self.lambtha, k)) / factorial)
    
    def cdf(self, k):
        if k < 0:
            return 0
        
        cumulative = 0
        for x in range(0, int(k) + 1):
            cumulative += self.pmf(x)

        return cumulative
        
if __name__ == '__main__':
    np.random.seed(0)
    data = np.random.poisson(5., 100).tolist()
    p1 = Poisson(data)
    print('Lambtha:', p1.lambtha)

    p2 = Poisson(lambtha=5)
    print('Lambtha:', p2.lambtha)
