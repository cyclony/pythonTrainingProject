class Sentence:
    words = None
    def __init__(self, string):
        self.words = string.split()

    def __getitem__(self, item):
        return self.words[item]

    def __len__(self):
        return len(self.words)


s = Sentence("cyc love Easta")
for x in s:
    print(x)
print(s[1])

it = iter(s)
print(next(it))
print(next(it))

