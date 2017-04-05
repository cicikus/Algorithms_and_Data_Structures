def scope_test():
	def do_local():
		spam = "local spam"

	def do_nonlocal():
		nonlocal spam
		spam = "nonlocal spam"

	def do_global():
		global spam
		global bebe
		spam = "global spam"
		bebe = "global bebe"
		# print("in do_global():", spam, bebe)

	spam = "test spam"
	do_local()
	print("After local assignment:", spam)
	do_nonlocal()
	print("After nonlocal assignment:", spam)
	do_global()
	print("After global assignment:", spam, bebe)

scope_test()
print("In global scope:", spam)