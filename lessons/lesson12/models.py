class Human:
    __current_id = 0
    def __init__(self, name, age, sex):
        self.id = self.__get_id()
        self.name = name
        self.age = age
        self.sex = sex
    @classmethod
    def __get_id(cls):
        cls.__current_id += 1
        return cls.__current_id
    def __str__(self):
        return f"name:{self.name} age:{self.age} sex:{self.sex}"

    def __repr__(self):
        return f"<{self.name}>"

    def to_dict(self):
        return {
            "id": self.id,
            "name": self.name,
            "age": self.age,
            "sex": self.sex
        }