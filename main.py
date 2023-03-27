class Variable:
    def __init__(self, name, value=None):
        self.name = name
        self.value = value


class Interpreter:
    def __init__(self):
        self.variables = {}

    def var_(self, code_line):
        parts = code_line.split()
        var_name = parts[1]
        var_value = None
        if len(parts) > 2:
            var_value = int(parts[-1])
        variable = Variable(var_name, var_value)
        self.variables[var_name] = variable
        print(f"Переменная {var_name} объявлена.")

    def print_(self, code_line):
        if code_line[-1] != ")":
            print("Syntax Errors: функция не закрыта )!")
        var_name = code_line.split("(")[1].replace(")", "")
        if var_name in self.variables:
            variable = self.variables[var_name]
            if variable.value is not None:
                print(variable.value)
            else:
                print(f"Переменная {var_name} не инициализирована.")
        else:
            print(f"Переменная {var_name} не найдена.")

    def execute(self, code_line):
        if code_line.startswith("var "):
            self.var_(code_line)
        elif code_line.startswith("Console.WriteLine"):
            self.print_(code_line)
        else:
            print("Неверная команда.")


if __name__ == "__main__":
    interpreter = Interpreter()
    while True:
        interpreter.execute(input(">> "))
