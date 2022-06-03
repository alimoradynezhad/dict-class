class DefaultDict(dict):
    def __init__(self, default_factory=None):
        super(DefaultDict, self).__init__()
        self.default_factory = default_factory

    def __getitem__(self, item):
        self.item = item
        s[item] = []
        return item




#         ...
s = DefaultDict(list)
s["pooya"]
s["ali"]
s["reza"]
s["farhad"]
print(s.values())
print(s.keys())
print(s)


