import os


def read_inputs(day):
    cwd = os.path.dirname(os.path.abspath(__file__))
    with open(os.path.join(cwd, day, "input_example")) as file:
        input_example = file.read()
    with open(os.path.join(cwd, day, "puzzle_input")) as file:
        puzzle_input = file.read()
    return input_example, puzzle_input

def read_inputs2(day, additional_input_number):
    cwd = os.path.dirname(os.path.abspath(__file__))
    inputs=[]
    for i in range(additional_input_number):
        with open(os.path.join(cwd, day, "input_example"+str(i+2))) as file:
            input_example = file.read()
            inputs.append(input_example)
    return inputs
