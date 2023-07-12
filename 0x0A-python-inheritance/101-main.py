#!/usr/bin/python3
add_attribute = __import__('101-add_attribute').add_attribute
check = __import__('101-add_attribute').is_builtin

# class MyClass():
#     pass


# mc = MyClass()
# add_attribute(mc, "name", "John")
# print(mc.name)

# try:
#     a = "My String"
#     add_attribute(a, "name", "Bob")
#     print(a.name)
# except Exception as e:
#     print("[{}] {}".format(e.__class__.__name__, e))

class MyClass(int):
    pass


a = MyClass()
add_attribute(a, "hbtn", "Holberton")
print(a.name)
