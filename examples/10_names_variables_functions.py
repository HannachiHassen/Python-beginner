# this one is like your scripts with argv
def print_two (*args):
    arg1, arg2 = args
    print(f"args1: {args1}, {args2}, {args3}")

# ok, that *args is actually pointless, we can just do this
def print_two_agian(arg, arg2):
    print(f"arg1: {arg1}, arg2:{arg2}")

# this just takes one argument
def print_one(arg):
    print(f"arg1:{arg1}")

# this one takes no argument
def print_none():
    print("I got nothing '_")

print_two("Zed","Shaw")
print_two_again("Zed","Shaw")
print_one('First!')
print_none()
