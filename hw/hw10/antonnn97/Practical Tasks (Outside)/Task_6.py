def change_class_name(cls, new_name):
    if new_name[0].isupper() and new_name.isalnum():
        new_class = type(new_name, (cls,), {})
        return new_class
    else:
        raise ValueError("Invalid class name. The name should start with an uppercase letter and contain only alphanumeric characters.")

# Test
class MyClass:
    pass

NewClass = change_class_name(MyClass, "UsefulClass")
print(NewClass.__name__)

AnotherClass = change_class_name(NewClass, "SecondUsefulClass")
print(AnotherClass.__name__)