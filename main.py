import json
from AppActionSelector import AppActionSelector
from AppDiskSelector import AppDiskSelector
from SystemCare.diskinfo import DiskInfo
from ActionParser import ActionParser
from CheckToRun import CheckToRun


def load_json_data(file_path):
    with open(file_path, "r") as file:
        data = json.load(file)
    return data


if __name__ == "__main__":
    actions = load_json_data("data.json")

    CheckToRun.check_system()

    selector = AppActionSelector(actions['actions'])
    answers = selector.select_actions()

    parser = ActionParser()
    parser.parse_and_run_actions(answers)
