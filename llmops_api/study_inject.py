from injector import Injector,inject

class A:
    pass

@inject
class B:
    def __init__(self,a:A):
        print("创建")
        self.a = a


test_injector = Injector()
b_instance = test_injector.get(B)



