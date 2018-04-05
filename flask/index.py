


class Parent(object):
    def __init__(self):
        self.name="parent";

    def say(self):
        print('Parent')



class Father(object):
    def __init__(self):
        self.name="father";

    def say(self):
        print('Father')


class Mother(Parent):

    def __init__(self):
        self.name="month";

class Child(Mother,Father):
    def __init__(self):
        super();
        pass;


child = Child();

print(child.mro())
