auctionAdmin=AuctionAdmin(starting_price=300)
    print(auctionAdmin.getAdminUser())
    #print(f"{auctionAdmin.getAdminUser} ")
    auction=AuctionHouse(int(input("Give starting price:")))
    user_name=str(input("enter username (Hint user name is User1):"))

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
            auction.make_commission_bid(commission_id,bid_amount)   
            #print(auction.comission_bids,auction.bidder_reference.admin1)