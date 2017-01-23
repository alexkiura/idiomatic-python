"""Idiomatic ways of working with directory paths."""

# Harmful
from datetime import date
import os

filename_to_archive = 'test.txt'
new_filename = 'test.bak'
target_directory = './archives'
today = date.today()
os.mkdir('./archives/' + str(today))
os.rename(filename_to_archive,
          target_directory + '/' + str(today) + '/' + new_filename)

# Idiomatic

current_directory = os.getcwd()
filename_to_archive = 'test.txt'
new_filename = os.path.splitext(filename_to_archive)[0] + '.bak'
target_directory = os.path.join(current_directory, 'archives')
today = date.today()
new_path = os.path.join(target_directory, str(today))
if os.path.isdir(target_directory):
    if not os.path.exists(new_path):
        os.mkdir(new_path)
    os.rename(
        os.path.join(current_directory, filename_to_archive),
        os.path.join(new_path, new_filename)
    )
