class LMS:
    def __init__(self ,library_name):
        self.library_name=library_name
        self.list_of_books="prac.txt"      
        self.book_dic={}
        id=10001
        with open(self.list_of_books) as f:
            content= f.readlines()
           
        for line in content :
            self.book_dic.update({str(id):{"book_title" : line.replace("\n"," "),"lender_name":" " ,"issue_date":" ","status" :"available" }})#this save file content in dic
            id=id+1

    def display(self):
        print("++++++++++++++++++++++++++++++++++++++++++++++++++++")
        print("book id \t\t  book title")
        print("++++++++++++++++++++++++++++++++++++++++++++++++++++")
        for key ,value in self.book_dic.items() :
            print(key , "\t",value.get("book_title"), "[",value.get("status"),"]")
        print("++++++++++++++++++++++++++++++++++++++++++++++++++++")
    def issue(self):
        book_id =input("Enter the book id =")
        lender_name=input("Enter the lender mame =  ")
        # check if book available 
        if  book_id in self.book_dic.keys():
            

            # book dedi kisi ko
            if not  self.book_dic[book_id]["status"]=="available":
                print("already issue to ",self.book_dic[book_id]["lender_name"])
                return self.issue()
         # book available hai
            elif  self.book_dic[book_id]["status"]=="available":
             
              self.book_dic[book_id]['lender_name']=lender_name
              self.book_dic[book_id]['status']="issued"
              print("book issued successfully")
                        
        else:
            print("INVALID ID !!!!")
            return self.issue() 
    def return_book(self):
       
        book_id = input("Enter the book id = ")
        if book_id in self.book_dic.keys():
            if self.book_dic[book_id]["status"] == "issued":
                self.book_dic[book_id]['lender_name'] = " "
                self.book_dic[book_id]['status'] = "available"
                print("Book returned successfully")
            else:
              print("This book is not issued to anyone.")
        else:
            print("INVALID ID !!!!")




try:
      
    lms=LMS("Prashant")
    
    prewss={"D":"dsiplay books","issue Book":"I","R":"return book","Q":"quit"}
    key_press= False
    while not (key_press=="q"):
        print(f"\n--------------- welcome to{lms.library_name} libraary management system--------")
        for key,value in prewss.items():
            print(key,"-",value)
        key_press=input("Enter your choice : ").lower()
        if key_press =="i":
            print("\ncurrent selection :")
            lms.issue()
        elif key_press =="d":
            print("\ncurrent selection :")
            lms.display()
        elif key_press =="r":
            print("\ncurrent selection : return")
            lms.return_book()                   
        elif key_press =="q":
            print("Thank you for using our library")
            break
except Exception as e:
    print("somthng goes shit")
