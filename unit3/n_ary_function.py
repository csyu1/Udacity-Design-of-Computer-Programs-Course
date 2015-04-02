def n_ary(f):
    """Given binary function f(x, y), return an n_ary function such
    that f(x, y, z) = f(x, f(y,z)), etc. Also allow f(x) = x."""
    def n_ary_f(x, *args):
        # your code here
        if len(args) == 0: return x
        if len(args) == 1: return f(x,args[0])
        return n_ary_f(x, n_ary_f(args[0], *args[1:]))
    return n_ary_f
    
def add(x,y):
    return x + y
f = n_ary(add)

print f(2, 1, 3, 4)