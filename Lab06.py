import _mysql


def oneQuery():
	db = _mysql.connect(host="localhost", user="root", passwd="Shane1124",db="books")
	db.query("""SELECT * FROM books;""")
	result = db.store_result()
	numrows = result.num_rows()
	while(numrows > 0):
					print(result.fetch_row())
					numrows = numrows - 1
	db.close()
	
def twoQuery():
	db = _mysql.connect(host="localhost", user="root", passwd="Shane1124",db="books")
	db.query("""SELECT * FROM authors;""")
	result = db.store_result()
	numrows = result.num_rows()
	while(numrows > 0):
					print(result.fetch_row())
					numrows = numrows - 1
	db.close()

def threeQuery():
	db = _mysql.connect(host="localhost", user="root", passwd="Shane1124",db="books")
	db.query("""SELECT A.booksName,B.storeName
	From books AS A,stores AS B,
	inventory As C
	WHERE C.booksID = A.booksID
	And C.storeID = b.storeID;""")
	result = db.store_result()
	numrows = result.num_rows()
	while(numrows > 0):
					print(result.fetch_row())
					numrows = numrows - 1
	db.close();


while buffer:
		print(""""
		0.Exit
		1.See books
		2.See authors
		3.See what books are available at which stores""")
		buffer=input("what would you like to do? ")
		if buffer == 1:
			oneQuery()
		if buffer == 2:
			twoQuery()
		if buffer == 3:
			threeQuery()
			
		
