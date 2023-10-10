import os
import shutil

def create_web_development_project():
    source_folder = r"./projects/web development"

    project_directory = input("Where do you want to create the project?: ")
    project_name = input("What is the name of your project: ")
    project_path = os.path.join(project_directory, project_name)

    os.mkdir(project_path)

    for item_name in os.listdir(source_folder):
        source = os.path.join(source_folder, item_name)
        destination = os.path.join(project_path, item_name)

        if os.path.isfile(source):
            shutil.copy(source, destination)
            print('copied', item_name)

        elif os.path.isdir(source):
            shutil.copytree(source, destination, symlinks=False, ignore=None)
            print('copied', item_name, 'and its contents')

create_web_development_project()