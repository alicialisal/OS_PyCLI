# PyCLI

Welcome to **PyCLI**, your personal command-line interface built with Python! This CLI application mimics basic Linux shell commands and introduces unique features to enhance your command-line experience. Dive in and explore the functionalities of PyCLI!

---

## Features

### Basic Commands
- **ls**: List files and directories in the current directory.
- **pwd**: Display the current working directory.
- **cd <directory>**: Change the current working directory.
- **mkdir <directory>**: Create a new directory.
- **rmdir <directory>**: Remove an empty directory.
- **touch <file>**: Create a new empty file.
- **rm <file>**: Remove a file.
- **cp <source> <destination>**: Copy a file.
- **mv <source> <destination>**: Move or rename a file or directory.
- **help**: Show a list of available commands.
- **clear**: Clear the terminal screen.
- **exit**: Exit the CLI.

### Unique Commands
- **search <pattern>**: Search for files or directories matching the given pattern.
- **tree**: Display the directory structure in a tree format.
- **find_large <size>**: Find files larger than the specified size (in bytes).
- **joke**: Display a random joke for your entertainment.

---

## How to Run PyCLI

1. **Clone the Repository**
   ```bash
   git clone <repository-url>
   cd <repository-folder>
   ```

2. **Run the Program**
   Ensure you have Python 3 installed on your system. Then, execute the following command:
   ```bash
   python3 pycli.py
   ```

3. **Start Using PyCLI**
   Once the program is running, type any command from the list above to interact with the CLI.

---

## Example Usage

### Basic Commands
```bash
CLI > ls
file1.txt
directory1

CLI > pwd
/home/user/projects/pycli

CLI > cd directory1
CLI > pwd
/home/user/projects/pycli/directory1
```

### Unique Commands
```bash
CLI > search file
/home/user/projects/pycli/file1.txt

CLI > tree
file1.txt
directory1
  file2.txt

CLI > find_large 1024
/home/user/projects/pycli/largefile.txt - 2048 bytes

CLI > joke
Why don’t skeletons fight each other? They don’t have the guts!
```

---

## Additional Notes

- **Platform Compatibility**: PyCLI works on Linux, macOS, and Windows (with minor adjustments for file paths).
- **Dependencies**: No external libraries are required; the program uses Python’s built-in libraries.
- **Exit the Program**: Type `exit` or press `Ctrl+C` to exit the CLI.

---

## Contribution
Feel free to fork this project, suggest new features, or report issues. Let’s make PyCLI even better together!

---

## License
This project is licensed under the MIT License. See the LICENSE file for details.

---

Enjoy using PyCLI! 🚀

