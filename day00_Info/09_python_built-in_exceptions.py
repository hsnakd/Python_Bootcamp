# Creating a sample text file for demonstration
with open('exception.txt', 'w') as file:
    file.write("Hello, this is a sample file.\nSecond line.\nThird line.")

# close(): Closes the file. You can't perform any file operations after closing it.
with open('exception.txt', 'r') as file:
    try:
        # ArithmeticError: Raised for errors in numeric calculations
        result = 10 / 0
    except ArithmeticError as e:
        print(f"ArithmeticError: {e}")

    try:
        # AssertionError: Raised when an assert statement fails
        assert False, "Assertion failed"
    except AssertionError as e:
        print(f"AssertionError: {e}")

    try:
        # AttributeError: Raised when attribute reference or assignment fails
        obj = None
        obj.method()
    except AttributeError as e:
        print(f"AttributeError: {e}")

    try:
        # EOFError: Raised when trying to read beyond the end of a file
        user_input = input("Enter something: ")
    except EOFError as e:
        print(f"EOFError: {e}")

    try:
        # FloatingPointError: Raised for floating-point operations that result in an error
        result = 1.0 / 0.0
    except FloatingPointError as e:
        print(f"FloatingPointError: {e}")

    try:
        # GeneratorExit: Raised when a generator's close() method is called
        def generator():
            try:
                yield 1
            finally:
                print("Generator closed")
                raise GeneratorExit("Closing generator")

        gen = generator()
        next(gen)
        gen.close()
    except GeneratorExit as e:
        print(f"GeneratorExit: {e}")

    try:
        # ImportError: Raised when an import statement fails
        import non_existent_module
    except ImportError as e:
        print(f"ImportError: {e}")

    try:
        # IndentationError: Raised when indentation is not correct
        if True:
            print("Indented block")
    except IndentationError as e:
        print(f"IndentationError: {e}")

    try:
        # IndexError: Raised when a sequence subscript is out of range
        my_list = [1, 2, 3]
        value = my_list[10]
    except IndexError as e:
        print(f"IndexError: {e}")

    try:
        # KeyError: Raised when a dictionary key is not found
        my_dict = {'key': 'value'}
        value = my_dict['nonexistent_key']
    except KeyError as e:
        print(f"KeyError: {e}")

    try:
        # KeyboardInterrupt: Raised when the user interrupts program execution (Ctrl+C)
        print("Press Ctrl+c or Ctrl+z to raise KeyboardInterrupt")
        while True:
            pass
    except KeyboardInterrupt:
        print("KeyboardInterrupt")

    try:
        # LookupError: Base class for exceptions that occur when a key or index is invalid
        raise LookupError("Custom LookupError")
    except LookupError as e:
        print(f"LookupError: {e}")

    try:
        # MemoryError: Raised when an operation runs out of memory
        big_list = [0] * (2**30)
    except MemoryError as e:
        print(f"MemoryError: {e}")

    try:
        # NameError: Raised when a local or global name is not found
        print(undefined_variable)
    except NameError as e:
        print(f"NameError: {e}")

    try:
        # NotImplementedError: Raised when an abstract method is not implemented
        class MyBaseClass:
            def my_abstract_method(self):
                raise NotImplementedError("Must be overridden in derived class")

        class MyDerivedClass(MyBaseClass):
            pass

        obj = MyDerivedClass()
        obj.my_abstract_method()
    except NotImplementedError as e:
        print(f"NotImplementedError: {e}")

    try:
        # OSError: Base class for I/O-related errors
        with open('nonexistent_file.txt', 'r') as file:
            pass
    except OSError as e:
        print(f"OSError: {e}")

    try:
        # OverflowError: Raised when an arithmetic operation exceeds the limits of its type
        result = 2 ** 1000
    except OverflowError as e:
        print(f"OverflowError: {e}")

    try:
        # ReferenceError: Raised when a weak reference object is used to access an object that no longer exists
        weak_ref = weakref.ref(None)
        obj = weak_ref()
    except ReferenceError as e:
        print(f"ReferenceError: {e}")

    try:
        # RuntimeError: Raised when an error is detected that doesn't fall into any other category
        raise RuntimeError("Custom RuntimeError")
    except RuntimeError as e:
        print(f"RuntimeError: {e}")

    try:
        # StopIteration: Raised when the next() function reaches the end of an iterator
        iterator = iter([1, 2, 3])
        while True:
            value = next(iterator)
            print(value)
    except StopIteration:
        print("StopIteration")

    try:
        # SyntaxError: Raised when a syntax error occurs
        exec("print 'Hello, world!'")
    except SyntaxError as e:
        print(f"SyntaxError: {e}")

    try:
        # TabError: Raised when indentation contains inconsistent use of tabs and spaces
        exec("def func():\n\tprint('Indented with tabs')")
    except TabError as e:
        print(f"TabError: {e}")

    try:
        # SystemError: Raised when the interpreter finds an internal error
        raise SystemError("Custom SystemError")
    except SystemError as e:
        print(f"SystemError: {e}")

    try:
        # SystemExit: Raised when sys.exit() is called
        sys.exit("Exiting the program")
    except SystemExit as e:
        print(f"SystemExit: {e}")

    try:
        # TypeError: Raised when an operation or function is applied to an object of an inappropriate type
        result = '5' + 5
    except TypeError as e:
        print(f"TypeError: {e}")

    try:
        # UnboundLocalError: Raised when a reference is made to a local variable before it is assigned
        def func():
            print(local_variable)
            local_variable = 10

        func()
    except UnboundLocalError as e:
        print(f"UnboundLocalError: {e}")

    try:
        # UnicodeError: Base class for all Unicode-related errors
        unicode_str = b'\x80abc'.decode('utf-8')
    except UnicodeError as e:
        print(f"UnicodeError: {e}")

    try:
        # UnicodeEncodeError: Raised when a Unicode-related error occurs during encoding
        unicode_str = 'é'
        encoded_str = unicode_str.encode('ascii')
    except UnicodeEncodeError as e:
        print(f"UnicodeEncodeError: {e}")

    try:
        # UnicodeDecodeError: Raised when a Unicode-related error occurs during decoding
        byte_str = b'\x80abc'
        decoded_str = byte_str.decode('utf-8')
    except UnicodeDecodeError as e:
        print(f"UnicodeDecodeError: {e}")

    try:
        # UnicodeTranslateError: Raised when a Unicode-related error occurs during translation
        unicode_str = 'é'
        translated_str = unicode_str.translate({233: 'e'})
    except UnicodeTranslateError as e:
        print(f"UnicodeTranslateError: {e}")

    try:
        # ValueError: Raised when a built-in operation or function receives an argument with the right type but an inappropriate value
        int_value = int('abc')
    except ValueError as e:
        print(f"ValueError: {e}")

    try:
        # ZeroDivisionError: Raised when the second argument of a division or modulo operation is zero
        result = 5 / 0
    except ZeroDivisionError as e:
        print(f"ZeroDivisionError: {e}")

# Note: You can't perform any file operations after closing it.
file.close()
