class MyList(list):
    def __init__(self, *args):
        super().__init__(args)

m = MyList(1, 2, 3)
for i in m:
    print(i)


d = {1: 2, 2: 3}
print((d.values()))
