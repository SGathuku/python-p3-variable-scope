name = "Joe"

def greeting(name):
    print(f"Hello, {name}")

greeting("Sam")  # Call the function


def practicing_function_scope():
  im_trapped_in_the_function = "You can't access me outside this function!"
  print(im_trapped_in_the_function)


# THE "global" KEYWORD
change_the_world = "change yourself"

def change_yourself():
    global change_the_world # Use the global keyword to change the value to a local scope.
                            # When you use this keyword, and run the code via python terminal, it will give "world changed".
    change_the_world = "world changed"
