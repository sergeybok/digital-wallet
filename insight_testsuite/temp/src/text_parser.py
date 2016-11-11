


class file_parser():

	def parse_file(self, filename):
		payments = []
		with open(filename,"r") as txt:
			next(txt)
			for l in txt:
				line = l.split(",")
				payments.append( (int(line[1]), int(line[2])) )
		return payments

	



