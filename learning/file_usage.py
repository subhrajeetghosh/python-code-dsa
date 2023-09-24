#  Copyright (c) 2023.
#  @Author Subhrajeet Ghosh

import os

path = "//Users//subhrgho//Documents//Programming//CodingFile//Test.rtf"

if os.path.exists(path):
    print("yes path exist!")
    if os.path.isfile(path):
        print("the path is a file!")
    elif os.path.isdir(path):
        print("the path is a folder!")
else:
    print("No")
