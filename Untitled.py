Python 3.6.0 (v3.6.0:41df79263a11, Dec 22 2016, 17:23:13) 
[GCC 4.2.1 (Apple Inc. build 5666) (dot 3)] on darwin
Type "copyright", "credits" or "license()" for more information.
>>> WARNING: The version of Tcl/Tk (8.5.9) in use may be unstable.
Visit http://www.python.org/download/mac/tcltk/ for current information.
a = {('Bob', 'A'), ('David', 'C'), ('Carol', 'B')}, 'Math-3A': {('Bob', 'B'), ('Alice', 'A')}
SyntaxError: invalid syntax
>>> 
>>> a = {('Bob', 'A'), ('David', 'C'), ('Carol', 'B')}, 'Math-3A': {('Bob', 'B'), ('Alice', 'A')}
SyntaxError: invalid syntax
>>> db = {'ICS-31': {('Bob', 'A'), ('David', 'C'), ('Carol', 'B')}, 'Math-3A': {('Bob', 'B'), ('Alice', 'A')}}
>>> for key in db.keys():
	for x, y in db[key]:
		print(x, y)
