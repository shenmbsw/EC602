                       

                             

class Polynomial():
    def __init__(self,value=[0]):
        self.p=value
        self.pp=dict()
        i=len(self.p)-1
        for y in self.p:
            if y != 0:
                self.pp[i]=y
            i-=1

    def __setitem__(self,key,value):
            self.pp[key]=value

    def __getitem__(self,key):
        if key in self.pp:
            return self.pp[key]
        else:
            return 0

    def __str__(self):
        return str(self.p)

        
    def __add__(self,value):
        result={}      
        for n in self.pp:
            if n in value.pp:
                result[n]=self.pp[n]+value.pp[n]
            else:
                result[n]=self.pp[n]
        for m in value.pp:
            if m in self.pp:
                result[m]=self.pp[m]+value.pp[m]
            else:
                result[m]=value.pp[m]
        return result
        
    def __sub__(self,value):
        sub=Polynomial()
        for n in self.pp:
            if n in value.pp:
                sub[n]=self.pp[n]-value.pp[n]
            else:
                sub[n]=self.pp[n]
        for n in value.pp:
            if (n in self.pp)==False:
                sub[n]=0-value.pp[n]
        return sub;
        
    def __mul__(self,value):
        prod={}
        for n in self.pp:
            for m in value.pp:
                if m+n in prod:
                    prod[m+n]=prod[m+n]+self.pp[n]*value.pp[m]
                else:
                    prod[m+n]=self.pp[n]*value.pp[m] 
        return prod

    def eval(self, value):
        sum = self
        for i in self.pp:
            sum[i] = self[i] * value**i
        return sum
        
    def __eq__(self,value): 
        if self.pp==value:
            return True
        else:
            return False
            
    def deriv(self):
        deriv=Polynomial()
        for n in self.pp:
             if n!=0:
                 deriv[n-1]=n*self.pp[n]
        return deriv


def main():
    p1 = Polynomial([1,3,5,7])
    print(p1)
    p1[3] = 4
    p1[0] = 9
    print(p1)
    p2 = Polynomial([1,2,3,4])
    print(p2)
    p3 = p1 + p2
    print(p3)
    print(p1)
    p4 = p1 - p2
    print(p4)
    p5 = p1 * p2
    print(p5)
    p6 = Polynomial([1,4,3])
    p7 = Polynomial([1,2,3])
    print(p3)
    print(p4)
    print(p5)
    print(p6)
    print(p7)
    print(p6 == p7)
    print(p1.deriv())


if __name__=="__main__":
    main()

