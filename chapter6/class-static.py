class A():
    count = 0
    def __init__(self):
        A.count += 1
    def exclaim(self):
        print("I'm an A!")
    @classmethod
    def kids(cls):
        print("A has,",cls.count,"little object.")
        
easy_a = A()
breezy_a = A()
wheezy_a = A()

A.kids()
A.count #cls.count inside = 3
#-------------------------------------
class CoyoteWeapon():
    @staticmethod
    def commercial():
        print("This CoyoteWeapon has been brought to you by Acme")
CoyoteWeapon.commercial()