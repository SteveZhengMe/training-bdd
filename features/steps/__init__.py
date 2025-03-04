# Import all py files from src directory dynamically

import importlib
import os


def import_all_modules_from_directory(directory, package):
    for root, _, files in os.walk(directory):
        for file in files:
            if file.endswith(".py") and file != "__init__.py":
                module_path = os.path.join(root, file)
                relative_path = os.path.relpath(module_path, directory)
                module_name = f"{package}.{relative_path.replace(os.sep, '.')[:-3]}"  # Remove .py extension
                importlib.import_module(module_name)


# Import all modules from subdirectories of 'src'
src_directory = os.path.join(os.path.dirname(__file__), "..", "..", "tests")
import_all_modules_from_directory(src_directory, "tests")
