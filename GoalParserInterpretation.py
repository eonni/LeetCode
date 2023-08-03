def inerpret(command):
    command = command.replace("(al)", "al")
    command = command.replace("()", "o")
    return command


command1 = inerpret("G()(al)")
command2 = inerpret("G()()()(al)")
print(command1)
print(command2)
