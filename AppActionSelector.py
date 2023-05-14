import inquirer
from pprint import pprint


class AppActionSelector:
    def __init__(self, actions):
        self.system_actions = actions
        self.actions = [(action['title'], action['name'])
                        for action in self.system_actions]

    def select_actions(self):
        questions = [
            inquirer.Checkbox(
                "actions",
                message="Select actions to run",
                choices=self.actions,
            ),
        ]

        answers = inquirer.prompt(questions)
        selected_actions = [
            action for action in self.system_actions if action['name'] in answers['actions']]
        return selected_actions
