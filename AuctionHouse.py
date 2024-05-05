from sre_compile import isstring


class AuctionHouse:
    comission_bids = []
    live_bidder={"C","750"}
    registered_users={"User1":"1234"}
    

    def __init__(self,starting_price) -> None:
        self.starting_price = starting_price
        self.comission_bids = []
        self.live_bidder =[]
        self.bidder_reference={"admin1":3,"C":1,"User1":2,"SysAdmin":4}
        self.registered_users = {"User1":"123"}
    
    def authentication_user(self,username,password):
        return username in self.registered_users and self.registered_users[username] == password
    
    def make_commission_bid (self, bidder_id, max_bid):
        self.comission_bids.append((bidder_id,max_bid))
    def place_live_bids(self,bidder_id,bid_amount):
        self.live_bidder.append((bidder_id,bid_amount))
class AuctionAdmin(AuctionHouse):
    def __init__(self,starting_price,comission_bids,live_bidder,bidder_reference):
        AuctionHouse.__init__(self,starting_price,comission_bids,live_bidder,bidder_reference)    
        self.admin_user={"admin1":"123"}

    def getAdminUser(self):
        return self.admin_user


if __name__=="__main__":
    auction=AuctionHouse(int(input("Give starting price:")))
    user_name=str(input("enter username (Hint user name is User1):"))

    number_of_commissionbidder=int(input("enter the number of Bidder as Commision:"))
    #print(f"{user_name} \n and {number_of_commissionbidder}")
    for x in range(number_of_commissionbidder):
        # auction.make_commission_bid(str(input("enter A B C")),int(input("enter number:")))
        commission_id = input("enter X Y Z or A B :")
        bid_amount=int(input("enter number:"))
        if commission_id.isdigit():
            print("please enter string! Warning!")
            commission_id = input("enter X Y Z or A B :")
            if commission_id.isdigit():
                print("please restart the program")
                break
        elif isinstance(bid_amount,str):
            print("Please enter number!Warning!")
            bid_amount=int(input("enter number:"))
            if isinstance(bid_amount,str):
                print("please restart the program")
                break
        else:
            auction.make_commission_bid(commission_id,bid_amount)   
            #print(auction.comission_bids,auction.bidder_reference.admin1)