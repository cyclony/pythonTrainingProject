class Sentence:

    def __init__(self,s):
        self.s = s

    def __iter__(self):
        for word in self.s.split():# lazy version
            yield word



s = Sentence("hello world, this is for ET test")
it = iter(s)
print(next(it))
print(next(it))
print(next(it))
