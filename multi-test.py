#!/usr/bin/env python3

import subprocess

command = "pytest test_bayes.py"

for i in range(50):
    result = subprocess.Popen(command, shell=True,
                            stdout=subprocess.PIPE, stderr=subprocess.PIPE)

    output,error = result.communicate()

    if error:
        print (error)
        print('ERROR COUNT: ', i)
        exit(0)
    print(i)