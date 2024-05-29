from simulation import Simulation, GeneratorFactory
from generator import ExponentialGenerator, UniformGenerator

class ExponentialFactory(GeneratorFactory):
    
    def createArrivals(self):
        return ExponentialGenerator(1.0, self.number_of_samples, self.seed)
    
    def createServices(self):
        return ExponentialGenerator(0.7, self.number_of_samples, self.seed)
    
class UniformFactory(GeneratorFactory):
    
    def createArrivals(self):
        return UniformGenerator(0, 20, self.number_of_samples, self.seed)
    
    def createServices(self):
        return UniformGenerator(2, 5, self.number_of_samples, self.seed)

if __name__ == "__main__":
    title = 'Single queue single service simulation'
    number_of_samples = 1000
    app = Simulation(title, UniformFactory(number_of_samples))
    app.run()