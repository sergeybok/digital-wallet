README_Sergiy

run from root /digital-wallet like so:
$ python src/driver.py 
	args: 	-v = verbose gives running times for each part of the process
			-h = prints out which arguments are available, less detailed version of this
			-i ./paymo_input/stream_payment.txt = input stream file
			-b ./paymo_input/batch_payment.txt = input batch file to initialize network
	Input and batch files default to the ones above

My test suite can be ran via the command:
$ python src/tests.py
It contains unit tests for the various individual compenents of the backend such as adding payments, and seeing whether some set of degrees of separation work or not


I wrote this program in python 2.7 though I think 3 will work as well
I decided to use iterative deepening in order to find degrees of separation between nodes on a graph (implemented as a dictionary of lists)
NOTE: My original intuition was for floyd warshall (which would have been better in a static graph) but it was taking to long to add new payments and update the fw matrix


Run time isn't amazing but as far as I know iterative deepening is best algorithm for this.
Breadth first search might have been a tiny bit faster but it's more memory intensive hence deepening for large simultaneous batches of data seems smarter (since the runtime difference is minimal)

One degree of separation takes me about 25 secs to run on 3 million stream provided
Two degrees takes me ~35 secs
Four degrees take me ~40 secs