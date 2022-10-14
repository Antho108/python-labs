# Write a script that walks through a nested folder structure 
# and prints out all the Python files it can find.
# Run it in your labs folder and add formatting for nicer viewing.

import pathlib

path = pathlib.Path().cwd()

for filepath in path.iterdir():
    print(filepath)







# desktop = pathlib.Path('/Users/Ranganath/Desktop')
# # Create a new folder
# new_path = pathlib.Path('/Users/Ranganath/Desktop/Screens')
# new_path.mkdir(exist_ok=True)

# for filepath in desktop.iterdir():
#     # Filter for screenshots only
#     if filepath.suffix == '.jpeg':
#         # Create a new path for each file
#         new_filepath = new_path.joinpath(filepath.name)
#         # Move the screenshot there
#         filepath.replace(new_filepath)
# # Move the screenshots in there)