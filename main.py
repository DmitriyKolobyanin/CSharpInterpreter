class Interpreter:
    def __init__(self):
        self.variables = {}

    def declare_variable(self, code_line):
        parts = code_line.split()
        var_name = parts[1]
        var_value = int(parts[3]) if len(parts) > 3 else None
        self.variables[var_name] = var_value
        return f"Переменная {var_name} объявлена."

    def print_variable(self, code_line):
        if not code_line.endswith(")"):
            return "Syntax error: функция не закрыта )!"

        var_name = code_line.split("(")[1][:-1]
        if var_name not in self.variables:
            return f"Переменная {var_name} не найдена!"

        var_value = self.variables[var_name]
        if var_value is None:
            return f"Переменная {var_name} не инициализирована."
        return var_value

    def execute(self, code_line):
        if code_line.startswith("var "):
            return self.declare_variable(code_line)
        elif code_line.startswith("Console.WriteLine("):
            return self.print_variable(code_line)
        else:
            return "Неверная команда!"


if __name__ == "__main__":
    i = Interpreter()
    while True:
        print(i.execute(input()))
