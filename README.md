#Follow the following steps to use this package

1. Open command prompt and enter the following command:
	pip install topsis_101703129
2. Then import the library in your code using the following line:
	from topsis_101703129 import topsis
3. Using command line arguments:
  (i) Read the name of dataset file and values of weights and impacts, entered in the command prompt. Example of a code to do this:
	data = pd.read_csv(str(sys.argv[1]))
	weights = sys.argv[2].split(',')
	impacts = sys.argv[3].split(',')
  (ii) Then call the topsis function and pass the above variables as arguments to it:
	topsis.topsis(data,weights,impacts)
4. You will get the index of the best object on the command prompt.
