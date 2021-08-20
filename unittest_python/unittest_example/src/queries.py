class Query:

    def __init__(self, a, b, c):
        self.one = a + b
        self.two = c

    def c_div(self, x):
        return x / self.two

    def one_add(self, x):
        return x + self.one

def str_concat(str1, str2):
    return str1 + str2