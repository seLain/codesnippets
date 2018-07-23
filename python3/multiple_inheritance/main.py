class A:
	def foo(self):
		print('a')

class B:
	def foo(self):
		print('b')

class C:
	def foo(self):
		print('c')

class D:
	def foo2(self):
		print('d')

class E(A, B, C):
	def __init__(self):
		super()

class F(D, C, B):
	def __init__(self):
		super()

class G(A, B, C):
	def foo(self):
		super(G, self).foo()

e = E()
e.foo()

f = F()
f.foo()

g = G()
g.foo()