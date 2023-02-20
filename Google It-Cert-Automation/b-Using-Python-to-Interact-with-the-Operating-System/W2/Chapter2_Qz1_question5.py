import os

def parent_directory_new():
  # Create a relative path to the parent 
  # of the current working directory 
  relative_parent = os.path.join("..", "w")

  # Return the absolute path of the parent directory
  return os.path.abspath('..')

def parent_directory():
      # Create a relative path to the parent 
  # of the current working directory 
  relative_parent = os.path.join(os.getcwd(), os.pardir)

  # Return the absolute path of the parent directory
  return os.path.abspath(relative_parent)

print(f"Parent Dir.: {parent_directory()}")

def parent_directory_solo():
      # Create a relative path to the parent 
  # of the current working directory 
  relative_parent_cwd = os.getcwd()

  # Return the absolute path of the parent directory
  return os.path.abspath(relative_parent_cwd)

print(f"New Solo Dir.: {parent_directory_solo()}")

def parent_directory_parent():
      # Create a relative path to the parent 
  # of the current working directory 
  relative_parent_parent = os.pardir

  # Return the absolute path of the parent directory
  return os.path.abspath(relative_parent_parent)

print(f"New Parent Dir.: {parent_directory_new()}")

print(f"Relative Parent Dir.: {parent_directory_parent()}")