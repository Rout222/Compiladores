import lex

pos = 0
data = '1 + 2 * 3'
error = False

data = lex.lexIt(data)
def match(a):
	global pos
	if data[pos][0] == a:
		pos += 1
		return(data[pos][1])
	else:
		error = True

def number(n):
	#print("number")
	global pos
	if n[0] != 'INTEGER':
		error = True
	else:
		pos += 1
		return(n[1])

def S():
	#print("S")
	E()

def E():
	#print("E")
	T()
	Etail()
def Etail():
	#print("Etail")
	global pos
	if data[pos][0] == 'PLUS':
		match('PLUS')
		T()
		Etail()
	elif data[pos][0] == 'MINUS':
		match('MINUS')
		T()
		Etail()
	else:
		pass
		## pos += 1

def T():
	#print("T")
	F()
	Ttail()

def Ttail():
	#print("Ttail")
	global pos

	if data[pos][0] == 'TIMES':
		match('TIMES')
		F()
		Ttail()

	elif data[pos][0] == 'DIVIDE':
		match('DIVIDE')
		F()
		Ttail()
	else:
		pass
		## pos += 1

def F():
	#print("F")
	global pos
	if data[pos][0] == 'LPAREN':
		match('LPAREN')
		E()
		match('RPAREN')
	else:
		number(data[pos])
S()