class person:
    def __init__(self,name):
        self.name=name
    def hi(self):
        print( "hii",self.name)
p=person("sai")
p.hi()
#in
class parent:
    def func1(self):
        print("this is the function 1")
class child(parent):
    def func2(self):
        super().func1()
        print("this ")  
ob=child()
ob.func2()    