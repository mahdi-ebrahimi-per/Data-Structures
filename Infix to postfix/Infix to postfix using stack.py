# Python program to convert infix expression to postfix

# Class to convert the expression
class Infix_to_postfix:
	# Constructor to initialize the class variables
	def __init__(self, capacity):
		self.top = -1

        # ظرفیت
		self.capacity = capacity 
		
        # This array is used a stack
		self.array = []
		
        # Precedence setting / تنظیم اولویت ها 
		self.output = []
		self.precedence = {'+':1, '-':1, '*':2, '/':2, '^':3}
	
	# check if the stack is empty / چک کردن اینکه استک خالی است یا خیر
	def isEmpty(self):
		return True if self.top == -1 else False
	
	# Return the value of the top of the stack / برگرداندن آخرین ورودی استک
	def peek(self):
		return self.array[-1]
	
	# Pop the element from the stack / حذف آخرین ورودی استک
	def pop(self):
		if not self.isEmpty():   # empty -> not True : False : if False  / isn't empty -> not False : if True
			self.top -= 1
			return self.array.pop()  # آخرین آیتم حذف میشه و اون آیتم رو برمیگرداند
		else:
			return "$"
	
	# Push the element to the stack / اضافه کردن به استک
	def push(self, op):
		self.top += 1
		self.array.append(op)

	# A utility function to check is the given character is operand / چک کردن اینکه ورودی، عملگر است یا عملوند
	# 'A'.isalpha()  -> True   
	# 'A + B'.isalpha()  -> False   
	# '+'.isalpha()  -> False
	# ''.isalpha()  -> False
	def isOperand(self, ch):
		return ch.isalpha()

	# Check if the precedence of operator is strictly less than top of stack or not
	# چک میکند که ورودی که دادیم اولویتش با آخرین آیتم استک کوچک تر یا مساوی است یا خیر
	def notGreater(self, i):
		try:
			a = self.precedence[i]
			b = self.precedence[self.peek()]
			return True if a <= b else False
		except KeyError:
			return False
			
	# The main function that
	# converts given infix expression
	# to postfix expression
	# تبدیل میکند postfix رو به infix فانکشن اصلی که 
	def infixToPostfix(self, exp):
		
		# Iterate over the expression for conversion
		for i in exp:
			# If the character is an operand, add it to output
			# اگر اون حرفی که داریم اسکن میکنیم، عملوند بود، اون رو میریزیم تو خروجی
			if self.isOperand(i):
				self.output.append(i)
			
			# If the character is an '(', push it to stack
			# اگر آیتم اسکن شده، پرانتز باز بود، میندازیمش تو استک
			elif i == '(':
				self.push(i)

			# If the scanned character is an ')', pop and
			# output from the stack until and '(' is found
			elif i == ')':
				while( (not self.isEmpty()) and
								self.peek() != '('):
					a = self.pop()   # pop func, delete -1 index from list and return it
					self.output.append(a)
				if (not self.isEmpty() and self.peek() != '('):
					return 
				else:
					self.pop()

			# An operator is encountered
			else:
				while(not self.isEmpty() and self.notGreater(i)):
					self.output.append(self.pop())
				self.push(i)

		# pop all the operator from the stack
		while not self.isEmpty():
			self.output.append(self.pop())

		print("".join(self.output))

# Driver program to test above function
exp = "A/(B-C)*D+E"
obj = Infix_to_postfix(len(exp))
obj.infixToPostfix(exp)

