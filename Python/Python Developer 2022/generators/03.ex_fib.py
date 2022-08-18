
class FibGen():
    current = 0
    fn = 0
    fn1 = 1
    fn2 = 1
    def __init__(self, last):
        self.last = last

    def __iter__(self):
        return self

    def __next__(self):
        if FibGen.current == 0:
            num = FibGen.current            
            FibGen.current += 1
            return (f'Iteration:f{num} {FibGen.fn}')
        if FibGen.current == 1:
            num = FibGen.current
            FibGen.fn += 1
            FibGen.current += 1
            return (f'Iteration:f{num} {FibGen.fn}')
        if FibGen.current == 2:
            num = FibGen.current
            FibGen.current += 1
            return (f'Iteration:f{num} {FibGen.fn}')            
        if FibGen.current > 2 and FibGen.current <= self.last:
            num = FibGen.current
            FibGen.fn = FibGen.fn1 + FibGen.fn2
            FibGen.fn1 = FibGen.fn2
            FibGen.fn2 = FibGen.fn
            FibGen.current += 1
            return (f'Iteration:f{num} {FibGen.fn}')
        raise StopIteration

gen_list = []
gen = FibGen(30)
for i in gen:
    gen_list.append(i)
    print(i)

print(gen_list)
