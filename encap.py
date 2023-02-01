"""This class should make use of a private attribute or function.

This class should make use of a protected attribute or function.

Create an object that makes use of protected and private."""

#Class private
class Private:
    def __init__(self):
        #set private variable to 5
        self.__privatVar = 5
        #print private variable
        #use double underscore to access private variable
    def getPrivate(self):
        print(self.__privatVar)
        #use double underscore to access private variable
    def setPrivate(self, private):
        self.__privatVar = private
    def setProtected(self):
        def __init__(self):
            self._protectedVar = 0
    
obj = Private()
obj.getPrivate()
#reset variable to 12
obj.setPrivate(12)
obj.getPrivate()
obj = Private()
obj._protectedVar = 100
print(obj._protectedVar)

#program prints 5, then new variable 12
