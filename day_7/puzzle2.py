import os
from abc import ABC, abstractmethod
from typing import Self

class File(ABC):
    def __init__(self, name: str):
        self.name: str = name

    @abstractmethod
    def size(self) -> int:
        pass

class Directory(File):
    def __init__(self, name: str) -> None:
        super().__init__(name)

        self.files: list[File] = []
        self.parent: Self = None

    def cd(self, name: str) -> Self:
        if name == "..":
            return self.get_parent()
        
        for file in self.files:
            if isinstance(file, Directory) and file.name == name:
                return file
        
        self.files.append(Directory(name))
        return self.files[-1]

    def add(self, file: File):
        self.files.append(file)

    def size(self) -> int:
        directory_size: int = 0
        for file in self.files:
            directory_size += file.size()
        return directory_size
    
    def ls(self) -> list[File]:
        return self.files
    
    def set_parent(self, parent: Self) -> None:
        self.parent = parent
    
    def get_parent(self) -> Self:
        return self.parent

class TextFile(File):
    def __init__(self, name: str, size: int) -> None:
        super().__init__(name)
        self.size_ = size

    def size(self) -> int:
        return self.size_

class FileSystem():
    def __init__(self):
        self.root: Directory = None
        self.current_directory: Directory = None

    def get_root(self) -> Directory:
        return self.root
    
    def set_root(self, value: Directory) -> None:
        self.root = value
    
    def cd(self, name: str):
        if name == "/":
            self.current_directory = self.root
        else:
            next_directory = self.current_directory.cd(name)
            if next_directory.get_parent() == None:
                next_directory.set_parent(self.current_directory)

            self.current_directory = next_directory
        
        return self.current_directory
    
    def cwd(self) -> Directory:
        return self.current_directory

class TerminalParser():
    def __init__(self):
        pass

    def is_cd_command(self, input: str) -> bool:
        return input.startswith("$ cd")
    
    def is_ls_command(self, input: str) -> bool:
        return input.startswith("$ ls")

class FileFactory():
    def __init__(self):
        pass

    def create_file(self, input: str) -> File:
        if input.startswith("dir"):
            return Directory(input.split(" ")[1])
        
        return TextFile(input.split(" ")[1], int(input.split(" ")[0]))
        

answer = 0

root = Directory("/")
root.set_parent(root)

file_system = FileSystem()
file_system.set_root(root)

terminal_parser = TerminalParser()
file_factory = FileFactory()

with open(os.path.join(os.path.dirname(os.path.abspath(__file__)), "input.txt")) as puzzleInput:
    for line in puzzleInput:
        line = line.strip()
        if terminal_parser.is_cd_command(line):
            file_system.cd(line.split(" ")[2])
        elif terminal_parser.is_ls_command(line):
            continue
        else:
            file_system.cwd().add(file_factory.create_file(line))

max_storage_size = 70000000
update_size = 30000000
current_size = root.size()
size_to_delete = update_size - (max_storage_size - current_size)
answer = max_storage_size

def compute_answer(root: Directory):
    global answer
    size: int = 0
    for file in root.ls():
        size += file.size()

        if isinstance(file, Directory):
            compute_answer(file)
    
    if size < answer and size >= size_to_delete:
        answer = size

compute_answer(root)
print(answer)