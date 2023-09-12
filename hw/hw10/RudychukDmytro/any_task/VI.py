# DESCRIPTION:
# Timmy's quiet and calm work has been suddenly stopped by his project manager (let's call him boss) yelling:

# - Who named these classes?! Class MyClass? It's ridiculous! I want you to change it to UsefulClass!

# Tim sighed, he already knew it's gonna be a long day.
# Few hours later, boss came again:
# Much better - he said - but now I want to change that class name to SecondUsefulClass,

# and went off. Although Timmy had no idea why changing name is so important for his boss, he realized, that it's not the end, so he turned to you, his guru, to help him and asked you to prepare some function, which could change name of given class.
# Note: Proposed function should allow only names with alphanumeric chars (upper & lower letters plus ciphers), but starting only with upper case letter. In other case it should raise an exception.
# Disclaimer: there are obviously betters way to check class name than in example cases, but let's stick with that, that Timmy yet has to learn them.

def rename_class(old_class, new_name):

    if not new_name.isalnum() or not new_name[0].isupper():
        return print("New name is not correct")

    
    class_attrs = {}
    for attr_name in dir(old_class):
        attr = getattr(old_class, attr_name)
        if callable(attr):
            class_attrs[attr_name] = attr
        else:
            class_attrs[attr_name] = None


    new_class = type(new_name, (object,), class_attrs)

    return new_class


class MyClass:
    def __init__(self, value):
        self.value = value

    def print_value(self):
        print(self.value)

NewClass = rename_class(MyClass, "NewClass")

new = NewClass("First!")
new.print_value()


