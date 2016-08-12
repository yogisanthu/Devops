class Called:
    def __call__(self,*args,**kwargs):
        print ("I have been called",args,kwargs)
A = Called()
A('Ajay','Singh','kaphola',name='ajay',mn='singh')

