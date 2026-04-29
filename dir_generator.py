import os

def create_directory(root_name):
    # Check if the root directory already exists
    if not os.path.exists(root_name):
        os.makedirs(root_name)
        print(f"Directory '{root_name}' created successfully.")
    else:
        print(f"Directory '{root_name}' already exists.")

def create_subdirectories(root_name, subdirectories):
    # 'source' and 'test' are added to all projects automatically.
    if "source" not in subdirectories:
        subdirectories.append("source")
    if "test" not in subdirectories:
        subdirectories.append("test")
    for subdirectory in subdirectories:
        # Builds the full path without manual concatentation. (i.e. root_name + "/" + subdirectory)
        subdirectory_path = os.path.join(root_name, subdirectory)
        if not os.path.exists(subdirectory_path):
            os.makedirs(subdirectory_path)
            print(f"Subdirectories '{subdirectory}' created successfully.")
        elif subdirectory == "source" or subdirectory == "test":
            # Bypasses "already exists" message for 'source' and 'test'
            # Since 'source' and test are always attempted, 
            # an exist message would appear as an error when there wasn't one
            print(f"")
        else:
            print(f"Directory '{subdirectory}' already exists.")

def main():
    # Replace spaces with underscores to prevent OS path issues
    root_name = input("""
    Enter the name of the root directory:\n
    Note: Spaces will be replaced with underscores\n
    """).replace(" ", "_")
    print("")
    create_directory(root_name)

    # Protection for various spacings around commas
    # Steps: collapse double space -> remove space after comma -> remove remaining spaces -> split into list
    subdirectories = input("""
    Enter the names of the subdirectories:\n
    Example: source, test \n
    Note: If the source and test directories do not exist, they will be created automatically\n
    """).replace("  ", " ").replace(", ", ",").replace(" ", "").split(",")
    print("")
    create_subdirectories(root_name, subdirectories)
    
    
# Only runs when executed directly, not when imported as a module
if __name__ == "__main__":
    main()




