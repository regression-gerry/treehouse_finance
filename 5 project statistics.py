# print no. of code lines + comments
import sys
import os, os.path
import ast

# comment symbol 
comment = "#"

# extensions required, in this case, .py files
ext = ['.py']
if not ext:
    print('Pass required extension')

all_files = []
# set the directory to my-python-project 
for root, _, files in os.walk('.'):
    for f in files:
        fullpath = os.path.join(root, f)

        # check for git associations
        if '.git' not in fullpath:
            for extension in ext:
            	if fullpath.endswith(extension):
                    all_files.append(fullpath)

# a. count the amount of python files
print('No of .py files: {}'.format(len(all_files)))
print('Current directory: {}'.format(os.getcwd()))


if not all_files:
    print('Directory does not contain {} files'.format(ext[0]))

# b. count the numner of code and comment lines
# set the total counts for all files
line_count = 0
blank_lines = 0
comments  = 0

print('File\tcomment lines\tcode lines')

for file in all_files:
    with open(file) as f:

        # specific counts for file
        file_line_count = 0
        file_blank_lines = 0
        file_comments = 0

        for line in f:
            line_count += 1
            file_line_count += 1

            # check for whitespaces
            no_whitespace = line.strip()
            if not no_whitespace:
                blank_lines += 1
                file_blank_lines += 1
            
            # if it starts with '#'
            elif no_whitespace.startswith(comment):
                comments += 1
                file_comments += 1

        print(os.path.basename(file) + \
              "\t" + str(file_line_count) + \
              "\t" + str(file_blank_lines) + \
              "\t" + str(file_comments) + \
              "\t" + str(file_line_count - file_blank_lines - file_comments))



print('Summary for {}'.format('.')) # assuming the current dir is my_python_projects
print('--------------------')
print('Comment lines: ' + str(comments))
print('Code lines:    ' + str(line_count - blank_lines - comments))

# c. count total functions defined
class CountFunc(ast.NodeVisitor):
    func_count = 0
    def visit_FunctionDef(self, node):
        self.func_count += 1

total_func = []
for file in all_files:
    p = ast.parse(open(file).read())
    f = CountFunc()
    f.visit(p)
    total_func.append(f.func_count)

print('Total functions defined = {}'.format(sum(total_func)))

# c
# compare the parent head with HEAD-3
# git diff --stat HEAD^ HEAD-3

# d folder size
# get folder size
def get_size(path): 
    total_size = 0
    for dirpath, dirnames, filenames in os.walk(path):
        for f in filenames:
            fp = os.path.join(dirpath, f)
            # skip if it is symbolic link
            if not os.path.islink(fp):
                total_size += os.path.getsize(fp)

    return round(total_size/1000000, 2)

# first subfolders
subfolders_path = [f.path for f in os.scandir('.') if f.is_dir()]

# define secondary subfolders
# subdirectories may not have folders; look for those with folders
second_subfolders = []
for i in subfolders_path:
    for f in os.scandir(i):
        try:
            if f.is_dir():
                second_subfolders.append(f.path)
        except NameError:
            continue

# second_subfolders = [f.path for f in os.scandir(i) for i in subfolders_path if i.is_dir()]
# second_subfolders = list(set(second_subfolders))

print('{} size: {} mb'.format(os.getcwd(), get_size('.')))

for path in subfolders_path:
    print('{} size: {} mb'.format(path, get_size(path)))

for path in second_subfolders:
    print('{} size: {} mb'.format(path, get_size(path)))
