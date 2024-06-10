from functools import singledispatchmethod

class points:
    @singledispatchmethod
    def assign(self):
        raise NotImplementedError()

    @assign.register(int)
    def _(self,x,y):
        self.x=x
        self.y=y
        return self.x,self.y

    @assign.register (list)
    def _(self,a):
        self.x=a[0]
        self.y=a[1]
        return self.x,self.y
    
    @assign.register (dict)
    def _(self,D):
        self.x=D['x']
        self.y=D['y']
        return self.x,self.y

point1=points().assign(5,3)
point2=points().assign([3,5])
point3=points().assign({'x':2, 'y':3})
print(point1)
print(point2)
print(point3)