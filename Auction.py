class AuctionHouse:
    def __init__(self, starting_price):
        self.starting_price = starting_price
        self.commission_bids = []  # List to store commission bids
        self.live_bids = []  # List to store live bids during the auction
        self.bidder_references = {}  # Dictionary to maintain reputation references
        self.registered_users = {"User1": "123"}  # Dictionary to store registered users (username: password)

    def authenticate_user(self, username, password):
        """ Authenticate user based on username and password """
        return username in self.registered_users and self.registered_users[username] == password

    def place_commission_bid(self, bidder_id, max_bid):
        self.commission_bids.append((bidder_id, max_bid))

    def place_live_bid(self, bidder_id, bid_amount):
        self.live_bids.append((bidder_id, bid_amount))

    def handle_auction(self):
        current_price = self.starting_price
        for bidder_id, max_bid in self.commission_bids:
            if max_bid >= current_price:
                current_price = max_bid

        for bidder_id, bid_amount in self.live_bids:
            if bid_amount > current_price:
                current_price = bid_amount
                print(f'Bidder {bidder_id} bids {bid_amount} Kr')

        print('Sold!')

if __name__ == "__main__":
    auction = AuctionHouse(starting_price=500)

    # Place commission bids
    auction.place_commission_bid('A', 500)
    auction.place_commission_bid('B', 700)

    # Place live bids during the auction
    auction.place_live_bid('C', 600)
    auction.place_live_bid('C', 700)
    auction.place_live_bid('C', 750)

    # Online user (User1) tries to place a bid (requires authentication)
    username = "22"
    password = "123"

    if auction.authenticate_user(username, password):
        auction.place_live_bid(username, 800)
        auction.handle_auction()
    else:
        username= str(input("Enter username:"))
        
        print("Authentication failed. User cannot place bid.")

    # Handle the auction to determine the winner
    #auction.handle_auction()
