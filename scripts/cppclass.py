import os
import sys

if len(sys.argv) < 2:
    print("Please specify a filename.")
    sys.exit(1)

filename = sys.argv[1]

# Create the .cpp file
cpp_file = f"{filename}.cpp"
with open(cpp_file, 'w') as f:
    f.write(f"#include \"includes/{filename}.h\"\n\n")

# Create the header file
header_file = os.path.join('includes', f"{filename}.h")
with open(header_file, 'w') as f:
    class_name = filename.capitalize()
    f.write(f"#pragma once\n\nclass {class_name} {{\npublic:\n    {class_name}();\n    ~{class_name}();\n}};")
