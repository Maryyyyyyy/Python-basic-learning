# my_min() takes two arguments and returns the smaller one
# improve the function so that it can take any number of variables, so that the function call works

def my_min(x,*args):
    if x < min(args):
        return x
    else:
        return min(args)

print(my_min(8,13,4,42,120,7))