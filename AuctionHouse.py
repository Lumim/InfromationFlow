from sre_compile import isstring
class AuctionHouse:
    def __init__(self,starting_price):
        self.starting_price = starting_price
        self.comission_bids = []
        self.live_bidder ={}
        self.user_reference={"admin1":3,"C":1,"User1":2,"SysAdmin":4,"L":0}
        self.registered_users = {"User1":"1234"}
    
    def authentication_user(self,username,password):
        return username in self.registered_users and self.registered_users[username] == password
    
    def make_commission_bid (self, bidder_id, max_bid):
        self.comission_bids.append((bidder_id,max_bid))
    def place_live_bids(self,bidder_id,bid_amount):
        self.live_bidder.append((bidder_id,bid_amount))
class AuctionAdmin(AuctionHouse):
    def __init__(self,starting_price=0):
        super().__init__(starting_price)    
        self.admin_user={"admin1":"1234"}

    def getAdminUser(self):
        #print(self.admin_user)
        print(self.admin_user)
    def getAuthenticate(self,username,password):
        return username in self.admin_user and self.admin_user[username]==password


if __name__=="__main__":
    action=int(input("Enter 1 for use as admin or O as SystemAdmin"))
    if action==1:
        username=input("Enter Admin username:")
        password=input("Enter Admin password:")
        auctionAdmin=AuctionAdmin(starting_price=300)
        if(auctionAdmin.getAuthenticate(username,password)):
            print(auctionAdmin.getAdminUser())
            #auction started!
            auction=AuctionHouse(int(input("Give starting price:")))
            number_of_commissionbidder=int(input("enter the number of Bidder as Commision:"))
            #print(f"{user_name} \n and {number_of_commissionbidder}")
            for x in range(number_of_commissionbidder):
                # auction.make_commission_bid(str(input("enter A B C")),int(input("enter number:")))
                commission_id = input("Enter Bidder commission as one Character name like A B C :")
                bid_amount=int(input("Enter commision:"))
                if commission_id.isdigit():
                    print("please enter string! Warning next time abort!")
                    commission_id = input("Enter Bidder commission as one Character name like A B C :")
                    if commission_id.isdigit():
                        print("please restart the program")
                        break
                elif isinstance(bid_amount,str):
                    print("Please enter commision as a number/digit !Warning next time abort!")
                    bid_amount=int(input("Enter commision:"))
                    if isinstance(bid_amount,str):
                        print("please restart the program")
                        break
                else:
                    auction.make_commission_bid(commission_id,bid_amount,username)   
                    #print(auction.comission_bids,auction.bidder_reference.admin1)
        else:
            print("Authentication Error") 

    elif action==2 :
        pass
    else:
        print("system aborted")

