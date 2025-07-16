import os

def create_directory(root_name):
    if not os.path.exists(root_name):
        os.makedirs(root_name)
        print(f"Directory '{root_name}' created successfully.")
    else:
        print(f"Directory '{root_name}' already exists.")

def create_subdirectories(root_name, subdirectories):
    if "source" not in subdirectories:
        subdirectories.append("source")
    if "test" not in subdirectories:
        subdirectories.append("test")
    for subdirectory in subdirectories:
        subdirectory_path = os.path.join(root_name, subdirectory)
        if not os.path.exists(subdirectory_path):
            os.makedirs(subdirectory_path)
            print(f"Subdirectories '{subdirectory}' created successfully.")
        elif subdirectory == "source" or subdirectory == "test":
            print(f"")
        else:
            print(f"Directory '{subdirectory}' already exists.")

def main():
    root_name = input("""
    Enter the name of the root directory:\n
    Note: Spaces will be replaced with underscores\n
    """).replace(" ", "_")
    print("")
    create_directory(root_name)

    subdirectories = input("""
    Enter the names of the subdirectories:\n
    Example: source, test \n
    Note: If the source and test directories do not exist, they will be created automatically\n
    """).replace("  ", " ").replace(", ", ",").replace(" ", "").split(",")
    print("")
    create_subdirectories(root_name, subdirectories)
    
    

if __name__ == "__main__":
    main()




