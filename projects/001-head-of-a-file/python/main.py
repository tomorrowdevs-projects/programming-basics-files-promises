import sys
import os

command = sys.argv
script = os.path.basename(__file__)
suggested_options = ("\nOptions:\nscript.py -n <number of lines> file.txt:          Change the number of lines in the "
                     "output, add the -n (--lines) argument before the file name\nscript.py -v -n <number of lines> "
                     "file.txt:          Display the file name before outputting the specified lines with the -v "
                     "argument before the file name and the other options.\nscript.py -d file.txt file.txt:"
                     "                 Display the first lines of multiple files using a single command\n"
                     )


def read_lines(number, path):
    try:
        with open(path, 'r') as f:
            lines = f.readlines()

        called_lines = lines[:number]

        for line in called_lines:
            print(line)
    except OSError:
        print('cannot open', path)

    return ""


def single_file(path_file, option):
    length_command = 3
    if option == "-v" or option == "-d":
        length_command += 1
    if os.path.exists(path_file):
        if len(command) == length_command:
            print(read_lines(10, path_file))

        if len(command) == length_command + 1:
            try:
                number = int(command[-2])
                if number <= 0:
                    raise ValueError("Enter number greater than zero!")
                else:
                    print(read_lines(number, path_file))

            except ValueError:
                print("Command error!")
                print(suggested_options)
    else:
        raise FileNotFoundError("File not found!")
    return ""


def read_files():
    if "".join(command) == script or len(command) < 3:
        print(suggested_options)

    else:

        if command[1] == "-v":

            if len(command) > 3:
                file = command[-1]
                cwd = os.getcwd()
                path = os.path.join(cwd, file)

                if os.path.exists(path):
                    print(file)
                    print(single_file(path, "-v"))

            else:
                print(suggested_options)

        if command[1] == "-n":
            file = command[-1]
            cwd = os.getcwd()
            path = os.path.join(cwd, file)
            print(single_file(path, "-n"))

        if command[1] == "-d":

            if len(command) > 2:
                # First file
                file = command[-2]
                cwd = os.getcwd()
                path = os.path.join(cwd, file)
                print(file)
                print(single_file(path, "-d"))

                # Second file
                file = command[-1]
                cwd = os.getcwd()
                path = os.path.join(cwd, file)
                print(file)
                print(single_file(path, "-d"))

            else:
                print(suggested_options)
    return ""


if __name__ == '__main__':
    print(read_files())
