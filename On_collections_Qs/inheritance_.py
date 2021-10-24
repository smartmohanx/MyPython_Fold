#Explain Inheritance in Python with an example.

'''
It is a process of getting properties from one class to
other class.

The class which is providing properties is called as a
super class or parent class or base class.

The class which is taking the properties is called as
sub class or child class or derived class.

Class is a collection of variables and methods.
'''
#EXAMPLE:

class version1:

    def updated_show(self,mobile_name,camera):
        print("initial version: 1.0")
        print("mobile name:",mobile_name)
        print("camera initial version of MP:",camera)


class version2(version1):

    def updated_show(self,add_game,social_plt1):
        super().updated_show('vivo v20 pro','48MP')
        print("----------sep line------------")
        print("New version: 2.0")
        print("New game added:",add_game)
        print("New communication platform is added:",social_plt1)

class  version3(version2):

    def updated_show(self, camera, browser,bugs):
        super().updated_show('pubg','Instagram')
        print("----------sep line------------")
        print("New version: 3.0")
        print("camera is updated:",camera)
        print("Chrome browser is added:",browser)
        print("Security and improvements:",bugs)


v3 = version3()
v3.updated_show('64MP','Google Chrome 1.3.01','all bugs are fixed :)')

