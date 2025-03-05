# Import all py files from src directory dynamically

# please note: the default python code implementation is under /features/steps directory.
# If we don't want to mix the feature files with the python code, like what I did in the demo, moving the python code to /tests/ folder, we need the dynamic import here.
# But it will make the code complex and it doesn't follow the industry best practice. We can discuss it later.
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
