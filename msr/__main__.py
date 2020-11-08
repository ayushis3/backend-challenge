import sys
# from .classmodule import MyClass
# from .funcmodule import my_function
def main():
    args = sys.argv[1:]
    print('number of args: {}'.format(len(args)))

    # verify number of inputs allowed
    
    for arg in args:
        print('passed argument: {}'.format(arg))
    # my_function('hello world')
    # my_object = MyClass('Thomas')
    # my_object.say_name()
if __name__ == '__main__':
    main()
