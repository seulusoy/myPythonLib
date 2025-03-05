# This is not the optimum code.
# I create this library for myself.
# Others can use on their own risk.
# Open to suggestions and collaborations.
# The operations are not controlled.

def calcParity128(a: int):
	a = (a&0xffffffffffffffff)^(a>>64)
	a = (a&0xffffffff)^(a>>32)
	a = (a&0xffff)^(a>>16)
	a = (a&0xff)^(a>>8)
	a = (a&0xf)^(a>>4)
	a = (a&0x3)^(a>>2)
	a = (a&0x1)^(a>>1)
	return a

def mMultiplyRC(M: list, N: list):
	result = []
	for m in M:
		r = 0
		for n in N:
			r += calcParity128(m,n)<<j
		result.append(r)
	return result

def mMultiplyRR(M: list, N: list):
	result = []
	for m in M:
		r = 0
		for i,n in enumerate(N):
			if (m&(1<<i))!=0:
				r += n
		result.append(r)
	return result

def mMultiplyCC(M: list, N: list):
	result = []
	for n in N:
		r = 0
		for i,m in enumerate(M):
			if (n&(1<<i))!=0:
				r += m
		result.append(r)
	return result

def mSquareRR(M: list):
	return mMultiplyRR(M,M)

def mSquareCC(M: list):
	return mMultiplyCC(M,M)

def multiplyRowMColV(M: list, a: int):
	result = 0
	for m in M:
		result += calcParity128(m&a)<<i
	return result

def multiplyColMColV(M: list, a: int):
	result = 0
	for i, m in enumerate(M):
		if a&(1<<i)!=0:
			result += m
	return result

def multiplyRowVRowM(a: int, M: list):
	result = 0
	for i, m in enumerate(M):
		if a&(1<<i)!=0:
			result += m
	return result

def multiplyRowVColM(M: list, a: int):
	result = 0
	for m in M:
		result += calcParity128(m&a)<<i
	return result
