""" Price an option by the trinomial lattice """

from TrinomialTreeOption import TrinomialTreeOption
import numpy as np

class TrinomialLattice(TrinomialTreeOption):
    
    def _setup_parameters_(self):
        super(TrinomialLattice, self)._setup_parameters_()
        self.M = 2*self.N+1
    
    def _initialize_stock_price_tree_(self):
        self.STs = np.zeros(self.M)
        self.STs[0] = self.S0 * self.u**self.N
        
        for i in range(self.M)[1:]:
            self.STs[i] = self.STs[i-1]*self.d
    
    def _initialize_payoffs_tree_(self):
        return np.maximum(
            0, (self.STs-self.K) if self.is_call
            else(self.K-self.STs))
    
    def __check_early_exercise__(self, payoffs, node):
        self.STs = self.STs[1:-1] # Shorten the ends of the list
        early_ex_payoffs = (self.STs-self.K) if self.is_call else(self.K-self.STs)
        payoffs = np.maximum(payoffs, early_ex_payoffs)
        
        return payoffs