

class network():
	def __init__(self):
		self.users = {}
	

	def update_edges(self, p1, p2):
		try:
			self.users[p1].add(p2)
		except KeyError:
			self.users[p1] = {p2}


	def add_payment(self, payment):
		self.update_edges(payment[0],payment[1])
		self.update_edges(payment[1],payment[0])


	def iddfs(self, payment, degree):
		if (payment[0] not in self.users):
			return False
		elif(payment[1] not in self.users):
			return False
	#	source = payment[0]
	#	dest = payment[1]
		if (len(self.users[payment[0]]) < len(self.users[payment[1]])):
			source = payment[0]
			dest = payment[1]
		else:
			source = payment[1]
			dest = payment[0]

		for depth in xrange(0,degree+1):
			found = self.dls(source, dest, depth)
			if found :
				return True
		return False

	def dls(self, source, dest, depth):
		if depth == 0 and source == dest:
			return True
		if depth > 0:
			for child in self.users[source]:
				found = self.dls(child, dest, depth-1)
				if found:
					return True
		return False





