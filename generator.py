import numpy as np
import matplotlib.pyplot as plt

class Generator:
    def __init__(self, size=1000, seed=None):
        self.size = size
        self.seed = seed
        self.rng = np.random.default_rng(seed)
        self.data = []
        self.index = 0

    def generate(self):
        pass

    def next(self):
        if self.index >= self.size:
            self.index = 0
        self.index += 1
        return self.data[self.index - 1]

    def plot_distribution(self):
        data = self.generate()
        plt.hist(data, bins='auto')
        plt.xlabel('Value')
        plt.ylabel('Frequency')
        plt.title('Probability Distribution')
        plt.grid(True)
        plt.show()

class UniformGenerator(Generator):
        def __init__(self, lower=0, upper=1, size=1000, seed=None):
            super().__init__(size, seed)
            self.lower = lower
            self.upper = upper

        def generate(self):
            self.data = self.rng.uniform(self.lower, self.upper, self.size)
            return self.data
        
class NormalGenerator(Generator):
    def __init__(self, mean=0, std=1, size=1000, seed=None):
        super().__init__(size, seed)
        self.mean = mean
        self.std = std

    def generate(self):
        self.data = self.rng.normal(self.mean, self.std, self.size)
        return self.data
    
class ExponentialGenerator(Generator):
    def __init__(self, scale=1, size=1000, seed=None):
        super().__init__(size, seed)
        self.scale = scale #měřítko nebo rychlost

    def generate(self):
        self.data = self.rng.exponential(self.scale, self.size)
        return self.data
    
class PoissonGenerator(Generator):
    def __init__(self, lam=1, size=1000, seed=None):
        super().__init__(size, seed)
        self.lam = lam  # Průměrná míra událostí, 
                        # Tento parametr udává průměrný počet událostí, které se očekávají v daném časovém intervalu.

    def generate(self):
        self.data = self.rng.poisson(self.lam, self.size)
        return self.data
    
class BinomialGenerator(Generator):
    def __init__(self, n=1, p=0.5, size=1000, seed=None):
        super().__init__(size, seed)
        self.n = n  # Počet pokusů
        self.p = p  # Pravděpodobnost úspěchu v jednom pokusu

    def generate(self):
        self.data = self.rng.binomial(self.n, self.p, self.size)
        return self.data
    
class BernoulliGenerator(Generator):
    def __init__(self, p=0.5, size=1000, seed=None):
        super().__init__(size, seed)
        self.p = p  # Pravděpodobnost úspěchu

    def generate(self):
        self.data = self.rng.binomial(1, self.p, self.size)
        return self.data
    
class GeometricGenerator(Generator):
    def __init__(self, p=0.5, size=1000, seed=None):
        super().__init__(size, seed)
        self.p = p  # Pravděpodobnost úspěchu

    def generate(self):
        self.data = self.rng.geometric(self.p, self.size)
        return self.data
    
class TriangularGenerator(Generator):
    def __init__(self, left=0, mode=0.5, right=1, size=1000, seed=None):
        super().__init__(size, seed)
        self.left = left
        self.mode = mode
        self.right = right

    def generate(self):
        self.data = self.rng.triangular(self.left, self.mode, self.right, self.size)
        return self.data
    
class LogisticGenerator(Generator):
    def __init__(self, loc=0, scale=1, size=1000, seed=None):
        super().__init__(size, seed)
        self.loc = loc
        self.scale = scale

    def generate(self):
        self.data = self.rng.logistic(self.loc, self.scale, self.size)
        return self.data
    
class LognormalGenerator(Generator):
    def __init__(self, mean=0, std=1, size=1000, seed=None):
        super().__init__(size, seed)
        self.mean = mean
        self.std = std

    def generate(self):
        self.data = self.rng.lognormal(self.mean, self.std, self.size)
        return self.data
    
class MultinomialGenerator(Generator):
    def __init__(self, n=1, pvals=[0.5, 0.5], size=1000, seed=None):
        super().__init__(size, seed)
        self.n = n
        self.pvals = pvals

    def generate(self):
        self.data = self.rng.multinomial(self.n, self.pvals, self.size).argmax(1)
        return self.data