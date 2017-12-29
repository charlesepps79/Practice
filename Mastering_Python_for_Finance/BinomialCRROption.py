""" Price an option by the binomial CRR model """
from BinomialAmericanOption import BinomialTreeOption
import math

class BinomialCRROption(BinomialTreeOption):
    def _setup_parameters_(self):
        self.u = math.exp(self.sigma * math.sqrt(self.dt))
        self.d = 1./self.u
        self.qu = (math.exp((self.r-self.div)*self.dt) - self.d)/(self.u-self.d)
        self.qd = 1-self.qu