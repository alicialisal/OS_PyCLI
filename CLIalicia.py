import os
import shutil
import random

class BasicCLI:
    def __init__(self):
        self.running = True

    def run(self):
        print("=" * 50)
        print("🌟 Welcome to PyCLI! 🌟")
        print("Your personal and interactive command-line interface.")
        print("\nFeatures:")
        print("- Manage files and directories effortlessly.")
        print("- Explore advanced commands like search, tree, and jokes!")
        print("- Type 'help' to see all available commands.")
        print("=" * 50)
        while self.running:
            try:
                command = input("CLI > ").strip()
                self.process_command(command)
            except KeyboardInterrupt:
                print("\nExiting CLI...")
                break


    def process_command(self, command):
        if not command:
            return
        parts = command.split()
        cmd = parts[0]
        args = parts[1:]

        if cmd == "ls":
            self.ls()
        elif cmd == "pwd":
            self.pwd()
        elif cmd == "cd":
            self.cd(args)
        elif cmd == "mkdir":
            self.mkdir(args)
        elif cmd == "rmdir":
            self.rmdir(args)
        elif cmd == "touch":
            self.touch(args)
        elif cmd == "rm":
            self.rm(args)
        elif cmd == "cp":
            self.cp(args)
        elif cmd == "mv":
            self.mv(args)
        elif cmd == "help":
            self.help()
        elif cmd == "clear":
            self.clear()
        elif cmd == "exit":
            self.exit()
        elif cmd == "search":
            self.search(args)
        elif cmd == "tree":
            self.tree()
        elif cmd == "find_large":
            self.find_large(args)
        elif cmd == "joke":
            self.joke()
        else:
            print(f"Unknown command: {cmd}")

    def ls(self):
        for item in os.listdir():
            print(item)

    def pwd(self):
        print(os.getcwd())

    def cd(self, args):
        if len(args) != 1:
            print("Usage: cd <directory>")
            return
        try:
            os.chdir(args[0])
        except FileNotFoundError:
            print("Directory not found.")

    def mkdir(self, args):
        if len(args) != 1:
            print("Usage: mkdir <directory>")
            return
        try:
            os.mkdir(args[0])
        except FileExistsError:
            print("Directory already exists.")

    def rmdir(self, args):
        if len(args) != 1:
            print("Usage: rmdir <directory>")
            return
        try:
            os.rmdir(args[0])
        except FileNotFoundError:
            print("Directory not found.")
        except OSError:
            print("Directory is not empty.")

    def touch(self, args):
        if len(args) != 1:
            print("Usage: touch <file>")
            return
        with open(args[0], 'w'):
            pass

    def rm(self, args):
        if len(args) != 1:
            print("Usage: rm <file>")
            return
        try:
            os.remove(args[0])
        except FileNotFoundError:
            print("File not found.")

    def cp(self, args):
        if len(args) != 2:
            print("Usage: cp <source> <destination>")
            return
        try:
            shutil.copy(args[0], args[1])
        except FileNotFoundError:
            print("Source file not found.")

    def mv(self, args):
        if len(args) != 2:
            print("Usage: mv <source> <destination>")
            return
        try:
            shutil.move(args[0], args[1])
        except FileNotFoundError:
            print("Source file not found.")

    def help(self):
        print("""
Available commands:
  ls            - List files and directories
  pwd           - Print working directory
  cd <dir>      - Change directory
  mkdir <dir>   - Create a new directory
  rmdir <dir>   - Remove an empty directory
  touch <file>  - Create a new empty file
  rm <file>     - Remove a file
  cp <src> <dst> - Copy a file
  mv <src> <dst> - Move or rename a file/directory
  search <pattern> - Search for files/directories by name
  tree          - Display directory structure as a tree
  find_large <size> - Find files larger than a certain size
  joke          - Display a random joke
  clear         - Clear the terminal screen
  exit          - Exit the CLI
        """)

    def clear(self):
        os.system('cls' if os.name == 'nt' else 'clear')

    def exit(self):
        self.running = False

    def search(self, args):
        if len(args) != 1:
            print("Usage: search <pattern>")
            return
        pattern = args[0]
        for root, dirs, files in os.walk(os.getcwd()):
            for name in dirs + files:
                if pattern in name:
                    print(os.path.join(root, name))

    def tree(self, path=".", indent=""):
        for item in os.listdir(path):
            item_path = os.path.join(path, item)
            print(f"{indent}{item}")
            if os.path.isdir(item_path):
                self.tree(item_path, indent + "  ")

    def find_large(self, args):
        if len(args) != 1:
            print("Usage: find_large <size>")
            return
        try:
            size_limit = int(args[0])
            for root, _, files in os.walk(os.getcwd()):
                for file in files:
                    file_path = os.path.join(root, file)
                    if os.path.getsize(file_path) > size_limit:
                        print(f"{file_path} - {os.path.getsize(file_path)} bytes")
        except ValueError:
            print("Invalid size value.")

    def joke(self):
        jokes = [
            "Why don’t skeletons fight each other? They don’t have the guts!",
            "What do you call cheese that isn't yours? Nacho cheese!",
            "Why couldn’t the bicycle stand up by itself? It was two tired!",
            "What do you get when you cross a snowman and a vampire? Frostbite!",
            "Why did the scarecrow win an award? Because he was outstanding in his field!"
        ]
        print(random.choice(jokes))

if __name__ == "__main__":
    cli = BasicCLI()
    cli.run()
