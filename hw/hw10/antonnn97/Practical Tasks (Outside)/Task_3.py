class Human:
    pass

class Man(Human):
    pass

class Woman(Human):
    pass

class God:
    @staticmethod
    def create():
        adam = Man()
        eve = Woman()
        return [adam, eve]

# Test
paradise = God.create()
print(f"Is the first object a Man? {isinstance(paradise[0], Woman)}")
print(f"Is the first object a Man? {isinstance(paradise[0], Man)}")