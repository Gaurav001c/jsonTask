#IMPORT JSON 
import json

#IMPORT MAIN FILE 
from Book import Book

while True:

    ###### MAIN JSON FILE READ AND RUNEVERY TIME #######
    with open("Books.json") as BooksJSONFile:
        try:
            booksJSONData = json.load(BooksJSONFile)
        except json.decoder.JSONDecodeError as e:
            print("JSONDecodeError:",e,"\nPlease Add Few Books First!!")
            
    ch = int(input("\nEnter Choice:\n1.Add Book\t\t2.Update Book\n3.Delete Book\t\t4.Show All Books\n5.Show All Authors\t6.Exit"))
    ########## INSERT DETA JSON FILE ########
    if ch == 1:
        print("\nADD BOOK")
        
        bid = int(input("Enter Book ID:"))
        bname = input("Enter Book Name:")
        authname = input("Enter Author Name:")
        bprice = int(input("Enter Book Price:"))

        #### PASS THE DETA BOOK FILE #####
        
        b = Book(bid,bname,authname,bprice)
        JSONFormatBook = b.getJSONFormatBook()

        ## CREATE A MAIN KEY ##
        booksJSONData[bid]=JSONFormatBook
        

        # DATA WAS ADD JSON FILE SUCESSFULLY #
        with open('Books.json','w') as BooksJSONFile:
            json.dump(booksJSONData,BooksJSONFile)
        print("Book Record Added!")

        
    ############# UPADTE DETA ###############   
    elif ch == 2:
        print("\nUPDATE BOOK")
        
        bid = input("Enter Book ID tot update:")
        bprice = int(input("Enter Book Updated Price:"))
        
        booksJSONData[bid]["bprice"] = bprice
        
        with open('Books.json','w') as BooksJSONFile:
            json.dump(booksJSONData,BooksJSONFile)
        print("Book Record Updated!")

    ############### DELETE DETA ################    
    elif ch == 3:
        print("\nDELETE BOOK")
        
        bid = input("Enter Book ID tot delete:")
        booksJSONData.pop(bid)
        
        with open('Books.json','w') as BooksJSONFile:
            json.dump(booksJSONData,BooksJSONFile)
            
        print("Book Record Deleted!")

    ############# SHOW DETA ####################    
    elif ch == 4:
        print("\n\t*** ALL BOOKS ***")

        count = 0
        for bid,book in booksJSONData.items():
                print(bid,book)

                count = count+1
                
                if count%10==0:
                    ch1 = input("\n\tDo you want to see next book (Y/N):-")
                    if ch1=='Y' or ch1=='y':
                        continue
                    else:
                        break
                        

                
                
        print("Showed all books!")

    ################## SHOW ALL AUTHER ############    
    elif ch == 5:
        print("\nSHOW ALL AUTHORS")

        
        for book in booksJSONData.values():
                print(book['authname'])
                
        print("Showed all authors!")

    ####### EXIT ############    
    elif ch == 6:
        print("\nExiting....")
        break

    ######### INVALID CHOICE ###########
    else:
        print("\nINVALID CHOICE..")
