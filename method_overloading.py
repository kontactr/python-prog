#method overloading...


from pythonlangutil.overload import Overload, signature

class A:
    a = 10
    def __init__(self,val):
    	self.a = val

    @Overload
    @signature("int")
    def sum_data(self,val):    
        print (self.a + val)

    @sum_data.overload
    @signature("int","int")
    def sum_data(self,val, i):
        print (self.a+val+i)

    

a1 = A(10)
a1.sum_data(10)
a1.sum_data(10,20)