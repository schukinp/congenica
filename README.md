Use framework [selene](https://github.com/yashaka/selene) (python selenium wrapper)

# Preconditions

* [Python 3+](https://www.python.org/)
* Browser [Chrome](https://www.google.com/chrome/)


# Installation

Install dependencies `pip install -r requirements`

# Start tests

`pytest test_tasks.py`

# Expected output

`````============================= test session starts ==============================
collecting ... collected 4 items

test_tasks.py::TestTasks::test_task_one 
test_tasks.py::TestTasks::test_task_two 
test_tasks.py::TestTasks::test_task_three 
test_tasks.py::TestTasks::test_task_four 

============================== 4 passed in 26.86s ==============================

Process finished with exit code 0
PASSED                           [ 25%]
MIDDLE
BOTTOM
LEFT
RIGHT

PASSED                           [ 50%]
Hello World!

PASSED                         [ 75%]
Element 0 = 1
Element 1 = 2
Element 2 = 3
Element 3 = 5
Element 4 = 7
Element 5 = 9

PASSED                          [100%]

