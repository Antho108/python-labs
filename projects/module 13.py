# Import pathlib
# Find the path to my Desktop
# List all the files on there
# Filter for screenshots only
# Create a new folder
# Move the screenshots in there

import pathlib
import posixpath

# pathlib.Path().cwd()  # Prints the path to your current working directory
# print(pathlib)

import pathlib


path = pathlib.Path("/Users/Ranganath/Desktop")
# for filepath in path.iterdir():
#     print(filepath.name)

# for filepath in path.iterdir():
# #     print(filepath.suffix)

# for filepath in path.iterdir():
#     if filepath.suffix == '.jpeg':  # Filter for screenshots only
#         print(filepath.name)
# import pathlib

# path = pathlib.Path().cwd()

# for filepath in path.iterdir():
#     print(filepath)

# Import pathlib
import pathlib

# Find the path to my Desktop
desktop = pathlib.Path('/Users/Ranganath/Desktop')
# Create a new folder
new_path = pathlib.Path('/Users/Ranganath/Desktop/Screens')
new_path.mkdir(exist_ok=True)

for filepath in desktop.iterdir():
    # Filter for screenshots only
    if filepath.suffix == '.jpeg':
        # Create a new path for each file
        new_filepath = new_path.joinpath(filepath.name)
        # Move the screenshot there
        filepath.replace(new_filepath)
# Move the screenshots in there