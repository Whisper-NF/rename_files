import os

# Directory containing the files to be renamed
directory = r'C:\Users\user\Desktop\folder'

filenames = os.listdir(directory)

num_files = len(filenames)

for i, filename in enumerate(filenames):
    
    extension = os.path.splitext(filename)[1]

    new_filename = str(i+1) + extension

    os.rename(os.path.join(directory, filename), os.path.join(directory, new_filename))

    # Print the progress bar
    progress = (i+1) / num_files
    print(f'\r[{"#" * int(progress * 20):<20s}] {int(progress * 100)}%', end='')

# Print the thank you message after the script finishes
print('\It has been completed!')
input()
