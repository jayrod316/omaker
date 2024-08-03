import os
import re


def main(input_dir, output_dir):
    dir_list = os.listdir(f"{input_dir}")
    for input_file in dir_list:
        new_folder = os.path.splitext(input_file)[0]
        os.makedirs(f"{output_dir}/{new_folder}", exist_ok=True)
        with open(f"{input_dir}/{input_file}") as contents:
            contents = contents.read()
            pattern = r"\n(?=O)|\n(?=<)"
            content_list = re.split(pattern, contents)
            for program in content_list:
                if program.startswith("O"):
                    program_name = re.match(r'O\d+\((.*)\)', program)[1]
                    program_name = filter_chars(program_name)
                    with open(f"{output_dir}/{new_folder}/{program_name}", "w") as new_program:
                        new_program.write(program)
                if program.startswith("<"):
                    program_name = re.match(r"<(.*)>", program).group(1)
                    program_name = filter_chars(program_name)
                    with open(f"{output_dir}/{new_folder}/{program_name}", "w") as new_program:
                        new_program.write(program)


def filter_chars(program_name):
    program_name = program_name.replace(".", "-")
    program_name = program_name.replace("/", "-")
    program_name = program_name.removeprefix("-")
    return program_name


if __name__ == "__main__":
    main("./input/", "./output/")
