from project_generator import ProjectGenerator

parent_directory = input("Where do you want to create the project?: ")
project_name = input("What is the name of your project?: ")

ProjectGenerator.create_web_development_project(parent_directory, project_name)