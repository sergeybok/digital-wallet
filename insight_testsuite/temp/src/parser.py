


class file_parser():

	def parse_file(filename):
		payments = []
		with open(filename,"r") as txt:
			next(txt)
			for l in txt:
				line = l.split(",")
				payments.append( (int(line[0]), int(line[1])) )
		return payments

	

	

