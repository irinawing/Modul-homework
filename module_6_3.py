class Hourse:
    def __init__(self):
        self.x_distance = 0 # длина
        self.sound = 'Frrr'

    def run(self, dx):
        self.x_distance += dx

class Eagle:
    def __init__(self):
        self.y_distance = 0 # высота
        self.sound = 'I train, eat, sleep, and repeat'

    def fly(self, dy):
        self.y_distance += dy

class Pegasus(Hourse, Eagle):
    def __init__(self):
        # Super(Hourse).__init__()  -- надо разобраться, как прописать Super()
        # Super(Eagle).__init__()
        Hourse.__init__(self)
        Eagle.__init__(self)

    def move(self, dx, dy):
        self.run(dx)
        self.fly(dy)

    def get_pos(self):
        return self.x_distance, self.y_distance

    def voice(self):
        print(self.sound)


p1 = Pegasus()

print(p1.get_pos())
p1.move(10, 15)
print(p1.get_pos())
p1.move(-5, 20)
print(p1.get_pos())

p1.voice()