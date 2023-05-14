import inquirer


class AppTypeSelector:
    def __init__(self, types):
        self.types = []
        for typ in types:
            key, value = list(typ.items())[0]
            self.types.append((value, key))

    def select_types(self, select_one=False):
        if select_one:
            questions = [
                inquirer.List(
                    "type",
                    message="Select a type to run",
                    choices=self.types,
                ),
            ]
        else:
            questions = [
                inquirer.Checkbox(
                    "types",
                    message="Select types to run",
                    choices=self.types,
                ),
            ]

        answers = inquirer.prompt(questions)

        if select_one:
            selected_type = [(value, key) for value, key in self.types if key == answers['type']]
            return selected_type[0] if selected_type else None

        selected_types = [(value, key) for value, key in self.types if key in answers['types']]
        return selected_types
