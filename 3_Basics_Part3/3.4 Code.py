Python 3.8.5 (tags/v3.8.5:580fbb0, Jul 20 2020, 15:57:54) [MSC v.1924 64 bit (AMD64)] on win32
Type "help", "copyright", "credits" or "license()" for more information.
>>> def glob_test():
	global bob

	
>>> def glob_test(arg1):
	global bob
	bob = arg1

	
>>> glob_test(3)
>>> bob
3
>>> def glob_test(6)
SyntaxError: invalid syntax
>>> glob_test(6)
>>> bob
6
>>> def string_cut(arg1):
	arg1 = arg1[:-1]

	
>>> string_cut("Hi")
>>> john = "Hi"
>>> string_cut(john)
>>> john
'Hi'
>>> def string_cut(arg1):
	arg1 -= arg1[-1]

	
>>> string_cut(john)
Traceback (most recent call last):
  File "<pyshell#21>", line 1, in <module>
    string_cut(john)
  File "<pyshell#20>", line 2, in string_cut
    arg1 -= arg1[-1]
TypeError: unsupported operand type(s) for -=: 'str' and 'str'
>>> def string_cut(arg1):
	arg1 = arg1.delete[-1]

	
>>> "hi".delete
Traceback (most recent call last):
  File "<pyshell#24>", line 1, in <module>
    "hi".delete
AttributeError: 'str' object has no attribute 'delete'
>>> 'hi'.del
SyntaxError: invalid syntax
>>> 'hi'.del(1)
SyntaxError: invalid syntax
>>> 'hi'.del[1]
SyntaxError: invalid syntax
>>> 'hi'.strip
<built-in method strip of str object at 0x000001C3D7FE34B0>
>>> 'hi'.strip(1)
Traceback (most recent call last):
  File "<pyshell#29>", line 1, in <module>
    'hi'.strip(1)
TypeError: strip arg must be None or str
>>> 'hi'.upper