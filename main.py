import os
import subprocess
import re

from folders_diff import compare_folders


def check_hw(hw_path):
    input_dir = f"{hw_path}/input"
    output_dir = f"{hw_path}/output"
    my_output_dir = f"{hw_path}/my_output"
    if not os.path.exists(my_output_dir):
        os.makedirs(my_output_dir)
    files_list = os.listdir(input_dir)
    for in_filename in files_list:
        assignment_no, question_no, test_no = parse_filename(in_filename)
        my_output_file = f"{my_output_dir}/{in_filename.replace('in','out')}"
        with open(f"{hw_path}/input/{in_filename}", 'r') as input_content_file:
            inputs = input_content_file.read()
        run_script_with_input(f"{hw_path}/hw{assignment_no}q{question_no}.py",inputs, my_output_file)
    compare_folders(my_output_dir, output_dir)

def parse_filename(filename):
    numbers = re.findall(r'\d+', filename)
    if len(numbers) != 3:
        raise ValueError(f"Expected 3 numbers, but found {len(numbers)} in string: {filename}")
    assignment_no, question_no, test_no = map(int, numbers)
    return assignment_no, question_no, test_no


def run_script_with_input(script_path, input_string, output_file):
    # Run the script and capture its output
    process = subprocess.Popen(['python', script_path],
                               stdin=subprocess.PIPE,
                               stdout=subprocess.PIPE,
                               stderr=subprocess.PIPE,
                               text=True)

    stdout, stderr = process.communicate(input_string)

    # Write the output to a file
    with open(output_file, 'w') as f:
        f.write(stdout)

    # If there were any errors, print them
    if stderr:
        print(f"Errors occurred:\n{stderr}")


if __name__ == '__main__':
    hw_path = "hw/hw1"
    check_hw(hw_path)
