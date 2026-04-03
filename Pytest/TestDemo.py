#FOR USING PYTEST WE HAVE TO NAME THE FOLDER USING TEST AND ALL THE FUNCTIONS THAT YOU CREATE MUST ALSO CONTAINS TEST
#THE FILES AND FUNCTION  NAMES THAT DOENT CONTAIN TEST CANT BE TESTED USING PYTEST WE CAN TEST THEM NORMALLY BUT NOT USING PYTEST
#to execute a file we can use two ways
# i.pytest TestDemo.py -v
# ii.pytest TestDemo.py -vs
# 1. -v → Verbose mode
from unittest import TestResult

import pytest


# pytest TestDemo.py -v(verbose)
# What it does:
# Shows detailed test names
# Shows PASS / FAIL status clearly
# But does NOT show print() output

# 2. -vs → Verbose + Show Output
# pytest TestDemo.py -vs
# What it does:
# Everything from -v
# PLUS shows print() statements output

#3.'s': stands for scripting it will print aall the print statements

#NOTE:PYTEST WILL NOT RECOGNISE THE FUNCTION THAT DOESNT FOLLOW THE RULES
#NOTE:IN CASE OF TEST CLAASES WE NEED NOT CREATE OBJECT AND CALL THE FUNCTION
# BUT IN CASE IF WE CREATE AN OBJECT AND CALL THE FUNCTIONS THEN IT WILL BE EXECUTED TWICE ONE THRPUGH PYTES AND ONE NORMALLY AS WE CREATOING OBJECT AND CALLING FUNCTIONS

# def test_login():
#     print("logging in..")
# def test_logout():
#     print("logging out..")
# def register():
#     print("Register in..")

# WE CANT MAKE CONSTRUCTOR OR CALL CONSTRUCTOR IN A CLASS WHILE USING PYTEST IT WILL GIVE A WARNING OR AN ERROR
# PYTEST IS A UNIT TESTING FRAMEWORK.THE RULES FOR
# 1.THE FILE NAME SHOULD START WITH test_ ot test
# 2.FILE AND function name should also start with test_ or test
# 3.CLASS NAME SHOULD START WITH Test
# WHEN WE FOLLOW THESE RULES PYTEST WILL AUTOMATICALLY RECOGNIZE THE FILES FUNCTIONS AND CLASSES FOLOOWING THE RULESSO WITHOUT GIVING FUNCTION CALLS WE CAN EXECUTE THE TEST FUNCTION AND WITHOUT CREATING AN OBJECT SWE CAN EXECUTE THE TEST CLASS

    # def __init__(self):
    #     print("Testdemo")
import pytest

@pytest.mark.regression
def test_fname():
    actual = True
    expected = True
    assert actual == expected, "Wrong"


@pytest.mark.regression
def test_fname1():
    actual = True
    expected = True
    assert actual == expected, "Wrong"


def test_fname2():
    print("false")

















