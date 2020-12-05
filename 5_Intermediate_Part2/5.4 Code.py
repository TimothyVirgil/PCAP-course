Python 3.9.0 (tags/v3.9.0:9cf6752, Oct  5 2020, 15:34:40) [MSC v.1927 64 bit (AMD64)] on win32
Type "help", "copyright", "credits" or "license()" for more information.
>>> class Vid_Game:
	def __init__(self,name,year,system)
	
SyntaxError: invalid syntax
>>> class Vid_Game:
	def __init__(self,name,year,system):
		self.name = input("What's the name of the game?")
		self.year = int(input("What's the year of release?"))
		self.system = input("What system was it released on?")

		
>>> zelda1 = Vid_game()
Traceback (most recent call last):
  File "<pyshell#8>", line 1, in <module>
    zelda1 = Vid_game()
NameError: name 'Vid_game' is not defined
>>> zelda1 = Vid_Game()
Traceback (most recent call last):
  File "<pyshell#9>", line 1, in <module>
    zelda1 = Vid_Game()
TypeError: __init__() missing 3 required positional arguments: 'name', 'year', and 'system'
>>> zelda1 = Vid_Game("The Legend of Zelda",1986,"Nintendo Entertainment System")
What's the name of the game?"The Legend of Zeld"
What's the year of release?1986
What system was it released on?Nes
>>> zelda1
<__main__.Vid_Game object at 0x000001B35B61C490>
>>> print(zelda1)
<__main__.Vid_Game object at 0x000001B35B61C490>
>>> zelda1.dict
Traceback (most recent call last):
  File "<pyshell#13>", line 1, in <module>
    zelda1.dict
AttributeError: 'Vid_Game' object has no attribute 'dict'
>>> zelda1.__dict__
{'name': '"The Legend of Zeld"', 'year': 1986, 'system': 'Nes'}
>>> class Video_Game:
	def __init__(self):
		self.name = input("What's the name of the game?")
		self.year = int(input("What's the year of release?"))
		self.system = input("What system was it released on?")

		
>>> zelda = Video_Game()
What's the name of the game?"The Legend of Zelda"
What's the year of release?1986
What system was it released on?Nintendo Entertainment System
>>> zedla.__dict__
Traceback (most recent call last):
  File "<pyshell#20>", line 1, in <module>
    zedla.__dict__
NameError: name 'zedla' is not defined
>>> zelda.__dict__
{'name': '"The Legend of Zelda"', 'year': 1986, 'system': 'Nintendo Entertainment System'}
>>> 