def class_name_changer(cls, new_name):
    if not new_name[0].isupper() or not new_name.isalnum():
        raise NameError('Invalid class name!')
    cls.__name__ = new_name