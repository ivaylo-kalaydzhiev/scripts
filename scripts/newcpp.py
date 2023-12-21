# Creates a C++ project with the .vscode and includes folder

import os
import sys
import shutil

# Check if project name is provided as argument
if len(sys.argv) < 2:
    print("Error: project name not provided.")
    sys.exit(1)

# Get project name from command-line argument
project_name = sys.argv[1]

# Create project directory
project_dir = os.path.join(os.getcwd(), project_name)
os.makedirs(project_dir, exist_ok=True)

# Create main C++ file
cpp_file = os.path.join(project_dir, "main.cpp")
with open(cpp_file, "w") as f:
    f.write(
        "#include <iostream>\n\nint main()\n{\n    std::cout << \"Hello, World!\" << std::endl;\n}")

# Create includes directory
includes_dir = os.path.join(project_dir, "includes")
os.makedirs(includes_dir, exist_ok=True)

# Create .vscode directory
vscode_dir = os.path.join(project_dir, ".vscode")
os.makedirs(vscode_dir, exist_ok=True)

# Copy tasks.json from ~/scripts/vscodeconfigs
tasks_src = os.path.join(os.path.expanduser("~"), "scripts", "vscodeconfigs", "tasks.json")
tasks_dst = os.path.join(vscode_dir, "tasks.json")
shutil.copyfile(tasks_src, tasks_dst)

# Copy launch.json from ~/scripts/vscodeconfigs
launch_src = os.path.join(os.path.expanduser("~"), "scripts", "vscodeconfigs", "launch.json")
launch_dst = os.path.join(vscode_dir, "launch.json")
shutil.copyfile(launch_src, launch_dst)