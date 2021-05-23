class Computer:
    def __init__(self,cpu,ram):
        self.cpu = cpu
        self.ram = ram

    def config(self):
        print("Config is " + self.cpu + " " + str(self.ram))

com1 = Computer('i5',512)

print(com1.config())