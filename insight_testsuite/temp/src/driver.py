from text_parser import file_parser
from FW import network
from datetime import datetime
from copy import copy
import getopt
import sys

def main(argv):

	#
	#
	batch_file = "./paymo_input/batch_payment.txt"
	stream_file = "./paymo_input/stream_payment.txt"
	verbose = False
	
	try:
		opts, args = getopt.getopt(argv,"vhb:i:")
	except getopt.GetoptError:
		print("Required: driver.py -i <input file>")
		print("Optional: driver.py -h (help) -v (verbose output to terminal) -b <batch file> ")
		sys.exit(2)
	for opt, arg in opts:
		if opt == '-h':
			print("Required: driver.py -i <input file>")
			print("Optional: driver.py -h (help) -v (verbose output to terminal) -b <batch file> ")
			sys.exit()
		elif opt == '-v':
			verbose = True
		elif opt == '-i':
			stream_file = arg
		elif opt == '-b':
			batch_file = arg

	if verbose:
    		def verboseprint(*args):
        		for arg in args:
        			print arg,
        		print
	else:   
		verboseprint = lambda *a: None


	net = network()
	parser = file_parser()

	verboseprint('Start batch parse file:\t' + str(datetime.now()))
	payments = parser.parse_file(batch_file)
	verboseprint('End batch parse file:\t' + str(datetime.now()))

	for p in payments:
		net.add_payment(p)

	verboseprint('End network init: \t'+ str(datetime.now()))

	payments_stream = parser.parse_file(stream_file)
	verboseprint('End stream file parse:\t'+ str(datetime.now()))
	verboseprint("Number of payments in stream:\t"+str(len(payments_stream)))
	out = ""
	out2 = ""
	out3 = "" 

	
	net1 = copy(net)
	verboseprint('Start stream processing 1 degree: \t'+ str(datetime.now()))
	for p in payments_stream:
		if net1.iddfs(p, 1):
			out += "trusted\n"
		else:
			out = "unverified\n"
		net1.add_payment(p)
	verboseprint('End stream processing 1 degree: \t'+ str(datetime.now()) +'\n')
	f = open("./paymo_output/output1.txt","w")
	f.write(out)
	f.close()

	net2 = copy(net)
	verboseprint('Start stream processing 2 degree: \t'+ str(datetime.now()))
	for p in payments_stream:
		if net2.iddfs(p,2):
			out2 += "trusted\n"
		else:
			out2 += "unverified\n"
		net2.add_payment(p)

	verboseprint('End stream processing 2 degree: \t'+ str(datetime.now())+'\n')
	f = open("./paymo_output/output2.txt","w")
	f.write(out2)
	f.close()


	verboseprint('Start stream processing 4 degree: \t'+ str(datetime.now()))
	for p in payments_stream:
		if net.iddfs(p,4):
			out3 += "trusted\n"
		else:
			out3 += "unverified\n"
		net.add_payment(p)

	verboseprint('End stream processing 4 degree: \t'+ str(datetime.now())+'\n')
	f = open("./paymo_output/output3.txt","w")
	f.write(out3)
	f.close()
		
			



if __name__ == "__main__":
	main(sys.argv[1:])


