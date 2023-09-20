def change_class_name(cls, new_name):
    if not new_name.isalnum():
        raise ValueError("The new name must contain only alphanumeric characters.")
    if not new_name[0].isupper():
        raise ValueError("The new name must start with an uppercase letter.")

    new_cls = type(new_name, cls.__bases__, dict(cls.__dict__))
    return new_cls
