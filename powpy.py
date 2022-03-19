import numpy as np

class PSN():
    def __init__(self, n_bus, b_data, l_data):
        self.n_bus = n_bus
        self.y_bus = np.zeros((n_bus, n_bus))        
        self.b_data = b_data
        self.l_data = l_data 

    def _y_bus(self):
        pass

    def y_bus(self):
        return self.y_bus


class Bus():
    def __init__(self, v=None, th=None, p=None, q=None):
        self.v  = v
        self.th = th
        self.p  = p
        self.q  = q

    def __repr__(self):
        return f"\nv={self.v}\nth={self.th}\np={self.p}\nq={self.q}\n"

