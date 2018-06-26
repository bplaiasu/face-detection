#  |-- alin-gheran
#  |   |-- 1.pgm
#  |   |-- ...
#  |   |-- 10.pgm
#  |-- s2
#  |   |-- 1.pgm
#  |   |-- ...
#  |   |-- 10.pgm
#  ...
#  |-- s40
#  |   |-- 1.pgm
#  |   |-- ...
#  |   |-- 10.pgm
#

import sys
import os.path


if __name__ == "__main__":      # http://ibiblio.org/g2swap/byteofpython/read/module-name.html
    if len(sys.argv) != 2:
        print("usage: create_csv <base_path>")
        sys.exit(1)

    BASE_PATH=sys.argv[1]
    SEPARATOR=";"

    label = 0
    f = open("images.csv", "w+")  # create test.csv file if it not already exists and write in it
    #f = open("images.csv", "a+")  # create test.csv file if it not already exists and write in it

    for dirname, dirnames, filenames in os.walk(BASE_PATH):
        for subdirname in dirnames:
            subject_path = os.path.join(dirname, subdirname)

            for filename in os.listdir(subject_path):
                abs_path = "%s/%s" % (subject_path, filename)
                #print("%s%s%d" % (abs_path, SEPARATOR, label))
                f.write("%s%s%d\r\n" % (abs_path, SEPARATOR, label))

            label = label + 1

    f.close()