import os
import shutil

def copy_project_contents(source_folder, parent_directory, project_name):
    project_directory = os.path.join(parent_directory, project_name)
    os.mkdir(project_directory)

    for item_name in os.listdir(source_folder):
        source = os.path.join(source_folder, item_name)
        destination = os.path.join(project_directory, item_name)

        if os.path.isfile(source):
            shutil.copy(source, destination)
            print('copied', item_name)

        elif os.path.isdir(source):
            shutil.copytree(source, destination, symlinks=False, ignore=None)
            print('copied', item_name, 'and its contents')


def create_web_development_project(parent_directory, project_name):
    source_folder = r"./projects/web development"
    copy_project_contents(source_folder, parent_directory, project_name)

parent_directory = input("Where do you want to create the project?: ")
project_name = input("What is the name of your project?: ")

create_web_development_project(parent_directory, project_name)

#TODO: create separate functions for each thing, maybe put everything into a class, and don't forget the error that happened because line 10 wasn't there