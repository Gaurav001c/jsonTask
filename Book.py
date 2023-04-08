
    ################# Fetch All Books Deta ###############
class Book:
    
    ############### Pass All Value ##############
    def __init__(self,bid,bname,authname,bprice):
        self.bid = bid
        self.bname = bname
        self.authname = authname
        self.bprice = bprice


    ####### CREATE KEY:VALUE DATA TO PASS JSON FILE ##########
    def getJSONFormatBook(self):
        JSONFormatBook = {"bid":self.bid, "bname":self.bname, "authname":self.authname, "bprice":self.bprice}
        return JSONFormatBook






