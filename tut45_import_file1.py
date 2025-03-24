"""
import sklearn as sk # sklearn comes under the global scope
import sys


print(sys.path) #To know the paths checked for importing modules

print(sk.__version__)
"""

from sklearn.ensemble import RandomForestClassifier
print(RandomForestClassifier())

import tut45_import_file2

"""
# We can import variables and functions and by writing the following we can use them directly as shown below
from tut45_import_file2 import a
print(a)
"""


print(tut45_import_file2.a) # better practice because here if variable "a" is also present in some other file then still it is clearly mentioned to refer to "a" of file(tut45_import_file2)

print(tut45_import_file2.print_quote("Beyond Divine"))