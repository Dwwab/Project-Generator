import os
import shutil

class ProjectGenerator:
    @staticmethod
    def get_project_directory(parent_directory: str, project_name: str) -> str:
        return os.path.join(parent_directory, project_name)

    @staticmethod
    def create_project_directory(parent_directory: str, project_name: str) -> None:
        os.mkdir(ProjectGenerator.get_project_directory(parent_directory, project_name))

    @staticmethod
    def copy_project_contents(source_folder: str, parent_directory: str, project_name: str) -> None:
        for item_name in os.listdir(source_folder):
            source = os.path.join(source_folder, item_name)
            destination = os.path.join(ProjectGenerator.get_project_directory(parent_directory, project_name), item_name)

            if os.path.isfile(source):
                shutil.copy(source, destination)
                print('copied', item_name)

            elif os.path.isdir(source):
                shutil.copytree(source, destination, symlinks=False, ignore=None)
                print('copied', item_name, 'and its contents')

    @staticmethod
    def create_web_development_project(parent_directory: str, project_name: str) -> None:
        source_folder = r"./projects/web development"
        ProjectGenerator.create_project_directory(parent_directory, project_name)
        ProjectGenerator.copy_project_contents(source_folder, parent_directory, project_name)