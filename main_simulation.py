from simulation import Simulation, GeneratorFactory
from generator import ExponentialGenerator, UniformGenerator, LogisticGenerator

class ExponentialFactory(GeneratorFactory):
    
    def createArrivals(self):
        return ExponentialGenerator(1.0, self.number_of_samples, self.seed)
    
    def createServices(self):
        return ExponentialGenerator(0.7, self.number_of_samples, self.seed)
    
class UniformFactory(GeneratorFactory):
    
    def createArrivals(self):
        return UniformGenerator(0.1, 5, self.number_of_samples, self.seed)
    
    def createServices(self):
        return UniformGenerator(0.1, 1, self.number_of_samples, self.seed)
    
class LogisticFactory(GeneratorFactory):
    
    def createArrivals(self):
        return LogisticGenerator(1, 0.2, self.number_of_samples, self.seed)
    
    def createServices(self):
        return LogisticGenerator(0.5, 0.1, self.number_of_samples, self.seed)

if __name__ == "__main__":
    title = 'Single queue single service simulation'
    number_of_samples = 1000
    app = Simulation(title, LogisticFactory(number_of_samples))
    app.run()
    app.show()