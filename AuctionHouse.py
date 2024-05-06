from sre_compile import isstring
class AuctionHouse:
    def __init__(self,starting_price):
        self.starting_price = starting_price
        self.commision_bids = []
        self.live_bidder ={('C',1000),('D',1400),('E',1450)}
        self.user_reference={"admin1":3,"C":1,"User1":2,"SysAdmin":4,"L":0}
        self.registered_users = {"User1":"1234"}
        self.system_admin_users={"sys1":"12345"}
    
    def authentication_user(self,username,password):
        return username in self.registered_users and self.registered_users[username] == password
    
    def make_commission_bid (self, bidder_id, max_bid,username):
        if self.user_reference[username]==3:
            self.commision_bids.append((bidder_id,max_bid))
        else:
            print("You are not Authenticated!!")
    def place_live_bids(self,bidder_id,bid_amount):
        self.live_bidder.append((bidder_id,bid_amount))
    
class AuctionAdmin(AuctionHouse):
    def __init__(self,starting_price=0):
        super().__init__(starting_price)    
        self.admin_user={"admin1":"1234","admin2":"1234"}

    def getAdminUser(self):
        print(self.admin_user)
    def getAuthenticate(self,username,password):
        return username in self.admin_user and self.admin_user[username]==password
    def deleteAdminUser(self,username):
        if username in self.admin_user:
            self.admin_user.pop(username)
            
        else:
            print( "user name not found")
    def changeAdminUserPassword(self,username,password):
        if username in self.admin_user :
            self.admin_user.update({username:password})
        else:
            print("No User matched with the username")
    def addAdminUser(self,username,password):
        if self.user_reference["sysAdmin"==4]:
            self.admin_user[username]=password
            print(f"the new admin user list is {self.admin_user}")
        else:
            print("not permited to the system")
            
    
    def handleAuction(self,commision_bids,current_price,live_bidder):
        for bidder_id, max_bid in commision_bids:
            if max_bid >= current_price:
                current_price = max_bid
        current_bidder_id=[]
        for bidder_id, bid_amount in live_bidder:
            if bid_amount > current_price:
                current_price = bid_amount
                current_bidder_id.append(bidder_id)
                print(f'Bidder {bidder_id} bids {bid_amount} Kr')
        print(f"Finally sold to {current_price}Kr to {current_bidder_id[-1]}")


if __name__=="__main__":
    action=int(input("Enter 1 for use as admin or 2 as SystemAdmin"))
    if action==1:
        username=input("Enter Admin username:")
        password=input("Enter Admin password:")
        auctionAdmin=AuctionAdmin(starting_price=300)
        if(auctionAdmin.getAuthenticate(username,password)):
            #print(auctionAdmin.getAdminUser())
            #auction admin part started!
            auction=AuctionHouse(int(input("Give starting price:")))
            number_of_commissionbidder=int(input("enter the number of Bidder as Commision Input can Be 1 or 2:"))
            #print(f"{user_name} \n and {number_of_commissionbidder}")
            for x in range(number_of_commissionbidder):
                # auction.make_commission_bid(str(input("enter A B C")),int(input("enter number:")))
                commission_id = input("Enter Bidder commission as one Character name like A or B:")
                bid_amount=int(input("Enter commision:"))
                if commission_id.isdigit():
                    print("please enter string! Warning next time abort!")
                    commission_id = input("Enter Bidder commission as one Character name like A or B :")
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
                    print(auction.commision_bids,auction.user_reference["admin1"])
            #auction function called
            auctionAdmin.handleAuction(auction.commision_bids,auctionAdmin.starting_price,auctionAdmin.live_bidder)
                

        else:
            print("Authentication Error") 

    elif action==2 :
        username=str(input("enter sys username Hint : sys pass 1234:"))
        if username in AuctionHouse(starting_price=0).system_admin_users:
            sys_action=int(input("Want to delete admin user press 1  or edit admin user press 2:"))
            auctionAdmin2=AuctionAdmin(starting_price=0)
            if sys_action==1:
                username=str(input(f"{auctionAdmin2.admin_user}\nType the username you want to delete from the list:"))
                auctionAdmin2.deleteAdminUser(username)
                print(f"Now the list is: {auctionAdmin2.admin_user} ")
            elif sys_action==2:
                username=str(input(f"{auctionAdmin2.admin_user}\nType the username you want to edit from the list:"))
                new_pass=str(input(f"{auctionAdmin2.admin_user}\nType the password you want to add for {username}:"))
                auctionAdmin2.changeAdminUserPassword(username,new_pass)
                print(f"Now the list is: {auctionAdmin2.admin_user} ")
            elif sys_action==3:
                username=str(input("add a username more that 4 char:"))
                password = str(input("add a password:"))
                auctionAdmin2.addAdminUser(username,password)
            else:
                print("wrong choice")

        else:
            print("system authentication failed.")
    else:
        print("system aborted")

