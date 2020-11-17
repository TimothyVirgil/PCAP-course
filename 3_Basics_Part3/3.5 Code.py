Python 3.8.5 (tags/v3.8.5:580fbb0, Jul 20 2020, 15:57:54) [MSC v.1924 64 bit (AMD64)] on win32
Type "help", "copyright", "credits" or "license()" for more information.
>>> #testing recursion
>>> def rec_prac(a):

	if a <= 0:
		return 'done'

	
>>> def rec_prac(a)
SyntaxError: invalid syntax
>>> def rec_prac(a):

	

	if a <= 0:
		return 'done'
	else:
		return rec_prac(a-1)

	
>>> count = 0
>>> rec_count = 0
>>> def rec_prac(a):

	global rec_count

	if a == 0:
		return (rec_count, 'done')
	else:
		rec_count += 1
		return (rec_prac(a-1))

	
>>> print(rec_prac(5))
(5, 'done')
>>> print(rec_prac(100))
(105, 'done')
>>> # my counter is not resetting... something to think about in future