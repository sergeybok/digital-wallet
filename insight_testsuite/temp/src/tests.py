import unittest
from text_parser import file_parser
from FW import network


class GraphTests(unittest.TestCase):

	def test_add_payment(self):
		net = network()
		p1 = 1234
		p2 = 4321
		payment = (p1, p2)
		net.add_payment(payment)
		self.assertTrue(p2 in net.users[p1])
		self.assertTrue(p1 in net.users[p2])
		self.assertTrue(net.iddfs(payment, 1))

	def test_no_connection(self):
		net = network()
		p1 = 1234
		p2 = 4321
		payment = (p1, p2)
		p3 = 2456
		p4 = 5321
		payment2 = (p3, p4)
		net.add_payment(payment)
		net.add_payment(payment2)
		test_payment = (p1,p3)
		test_payment2 = (p2,p4)
		self.assertFalse(net.iddfs(test_payment,1))
		self.assertFalse(net.iddfs(test_payment2,3))

	def test_2nd_degree(self):
		net = network()
		p1 = 1234
		p2 = 4321
		payment = (p1, p2)
		p3 = 2456
		payment2 = (p2,p3)
		net.add_payment(payment)
		net.add_payment(payment2)
		test_payment = (p1,p3)
		self.assertTrue(net.iddfs(test_payment,2))
		self.assertFalse(net.iddfs(test_payment,1))

	def test_3rd_degree(self):
		net = network()
		p1 = 1234
		p2 = 4321
		payment = (p1, p2)
		p3 = 2456
		p4 = 5432
		payment2 = (p2,p3)
		payment3 = (p3,p4)
		net.add_payment(payment)
		net.add_payment(payment2)
		net.add_payment(payment3)
		test_payment = (p1,p3)
		test_payment2 = (p1,p4)
		self.assertTrue(net.iddfs(payment,3))
		self.assertTrue(net.iddfs(test_payment,3))
		self.assertTrue(net.iddfs(test_payment2,3))
		test_payment3 = (p1,8888)
		self.assertFalse(net.iddfs(test_payment3,3))
		self.assertFalse(net.iddfs(test_payment2,2))


class ParserTests(unittest.TestCase):
	def test_parse(self):
		parser = file_parser()
		try:
			payments = parser.parse_file("../paymo_input/batch_payment.csv")
			payments = parser.parse_file("../paymo_input/stream_payment.csv")
			self.assertTrue(True)
			
		except:
			self.assertTrue(False)



if __name__ == '__main__':
	unittest.main()






