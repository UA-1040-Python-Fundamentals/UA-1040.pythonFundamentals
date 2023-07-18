print('Hello, my name Sebastiano, i`m here to help you with calculating.')
user_input= input('Write me what you need to calculate.In the format A + B: ')

deleteSpace = user_input.split()
deleteSpace = ''.join(deleteSpace)

calculated = eval(deleteSpace)

print(calculated)



