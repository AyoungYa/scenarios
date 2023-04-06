#!/bin/bash

mkdir lab lab/code lab/data lab/images && cd lab

touch a.c b.c c.c d.c main.cpp test.h test.cpp hello.py world.py code/a.c code/b.c code/c.c code/d.c code/main.cpp code/test.h code/test.cpp code/hello.py code/world.py data/a.txt data/b.txt data/c.txt data/d.txt images/a.jpg images/b.jpg images/c.jpg images/d.jpg

echo '#include <iostream>\nusing namespace std;\n' >> main.cpp
echo 'int main() \n{' >> main.cpp
echo '    cout << "hello world" << endl;' >> main.cpp
echo '    cout << "hello lanqiao" << endl;' >> main.cpp
echo '    return 0;' >> main.cpp
echo '}\n' >> main.cpp

# 安装 locate
sudo apt-get install locate
sudo updatedb
