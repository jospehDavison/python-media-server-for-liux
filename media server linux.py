import multiprocessing

boo = False

class newClass:
    
    def __init__(self, name):
        self.name = name
    
    def mainFunction(self):
        print("main")
        x= 0
        while x < 10:
            print(x)
            x += 1
    
    
    def secondFunction(self):
        print("sec")
        for x in range(10):
            print(x)
        boo = True


class1 = newClass("class1")

listProcs = []

listProcs.append(multiprocessing.Process(target=class1.mainFunction()))
listProcs.append(multiprocessing.Process(target=class1.secondFunction()))

for proc in listProcs:
    proc.start()

for proc in listProcs:
    proc.join()