import sys
import os

command = sys.argv
script = os.path.basename(__file__)
default_command = f"{script} head"
suggested_option = (f"{default_command} file.txt: displays the first 10 lines of a file;\n"
                    f"{default_command} -n <number> file.txt: change the number of lines in the output;\n"
                    f"{default_command} -v -n <number> file.txt: display the file name before outputting the specified "
                    f"lines;\n"
                    f"{default_command} -d first_file.txt second_file.txt: display the first lines of multiple files."
                    )


def search_file_txt(n):

    file_txt = command[n]
    directory = os.path.dirname(os.path.abspath(script))
    path_file = None

    while True:

        if file_txt in os.listdir(directory):
            path_file = os.path.join(directory, file_txt)
            break

        directory = os.path.dirname(directory)

        if directory == os.path.dirname(directory):
            break

    return path_file, file_txt


if len(command) < 3:
    raise ValueError(f"Invalid command! Options:\n{suggested_option}")

else:

    if " ".join(command[:2]) != default_command:
        raise ValueError(f"Invalid command! Options:\n{suggested_option}")

    else:

        if len(command) == 3:

            if command[-1] in ["-n", "-d", "-v"]:
                raise ValueError(f"Invalid command! Options:\n{suggested_option}")

            else:
                path = search_file_txt(-1)

            if path[0]:

                try:

                    with open(path[0], 'r') as f:
                        lines = f.readlines()

                    called_lines = lines[:10]

                    for line in called_lines:
                        print(line)

                except OSError:
                    print('cannot open', path[0])

            else:
                raise FileNotFoundError(f"{path[1]} not found!")

        elif len(command) == 5:

            if command[2] == "-n":
                number = command[-2]

                try:

                    number = int(number)
                    path = search_file_txt(-1)

                    if number <= 0:
                        raise ValueError("Number must be greater than zero!")

                except ValueError:
                    raise ValueError("Number must be greater than zero!")

                if path[0]:

                    try:

                        with open(path[0], 'r') as f:
                            lines = f.readlines()

                        called_lines = lines[:number]

                        for line in called_lines:
                            print(line)

                    except OSError:
                        print('cannot open', path[0])

                else:
                    raise FileNotFoundError(f"{path[1]} not found!")

            elif command[2] == "-d":

                if command[-2] in ["-n", "-d", "-v"]:
                    raise ValueError(f"Invalid command! Options:\n{suggested_option}")

                else:
                    path_1 = search_file_txt(-2)

                if path_1[0]:

                    try:

                        with open(path_1[0], 'r') as f:
                            lines = f.readlines()

                        called_lines = lines[:10]
                        print(command[-2])

                        for line in called_lines:
                            print(line)

                    except OSError:
                        print('cannot open', path_1[0])

                else:
                    raise FileNotFoundError(f"{path_1[1]} not found!")

                if command[-1] in ["-n", "-d", "-v"]:
                    raise ValueError(f"Invalid command! Options:\n{suggested_option}")

                else:
                    path_2 = search_file_txt(-1)

                if path_2[0]:

                    try:

                        with open(path_2[0], 'r') as f:
                            lines = f.readlines()

                        called_lines = lines[:10]
                        print(command[-1])

                        for line in called_lines:
                            print(line)

                    except OSError:
                        print('cannot open', path_2[0])

                else:
                    raise FileNotFoundError(f"{path_2[1]} not found!")

            else:
                raise ValueError(f"Invalid command! Options:\n{suggested_option}")

        elif len(command) == 6:

            default_command = default_command + " -v " + "-n"
            if " ".join(command[:4]) == default_command:
                number = command[-2]

                try:

                    number = int(number)
                    path = search_file_txt(-1)

                    if number <= 0:
                        raise ValueError("Number must be greater than zero!")

                except ValueError:
                    raise ValueError("Number must be greater than zero!")

                if path[0]:

                    try:

                        with open(path[0], 'r') as f:
                            lines = f.readlines()

                        called_lines = lines[:number]
                        print(command[-1])

                        for line in called_lines:
                            print(line)

                    except OSError:
                        print('cannot open', path[0])

                else:
                    raise FileNotFoundError(f"{path[1]} not found!")

            else:
                raise ValueError(f"Invalid command! Options:\n{suggested_option}")

        else:
            raise ValueError(f"Invalid command! Options:\n{suggested_option}")
