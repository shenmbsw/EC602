
class Polynomial():
    def __init__(self,sequence=None):
        self.D={}

        if sequence:
            N=len(sequence)
            for i,x in enumerate(sequence):
                if x:
                    self.D[N-i-1]=x

    def __add__(self,other):
        Sum=Polynomial()
        for coeff in self.D:
            Sum[coeff] = self.D[coeff]
        for coeff in other.D:
            Sum[coeff] += other.D[coeff]

        return Sum


    
    def __mul__(self,other):
        Prod=Polynomial()
        for i in self.D:
            for j in other.D:
                Prod[i+j] += self.D[i]*other.D[j]
        return Prod

    def __setitem__(self,key,value):
        if value:
            self.D[key] = value
        elif key in self.D:
                del self.D[key]

    def __getitem__(self,v):
        if v in self.D:
            return self.D[v]
        else:
            return 0

    def __eq__(self,other):
        return self.D == other.D

    def __str__(self):
        return "Polynomial({})".format(self.D)

    def __repr__(self):
        return str(self)

    def eval(self,x):
        t = 0
        for coeff in self.D:
            t += x**coeff * self.D[coeff]
        return t

    def deriv(self):
        P = Polynomial()
        for coeff in self.D:
            P[coeff-1] = self.D[coeff] * coeff
        return P

