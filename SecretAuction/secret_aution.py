from arts import logo, clear_console

print(logo)
print("Welcome to secret aution program.")

continue_bidding = True
bidders = {}

def get_highest_bidder(bidder_list):
    highest_bid = 0
    winner =""
    for bidder in bidder_list:
        if bidder_list[bidder] > highest_bid:
            highest_bid = bidder_list[bidder]
            winner = bidder
    
    print(f'The winner is {winner} with a bid of ${highest_bid}.')

while continue_bidding:

    name = input("What is your name?: ")
    bid = int(input("What is your bid?: $"))
    con = input("Are there any more bidders? Type 'yes' or no.\n" ).lower()

    bidders[name] = bid

    if con == 'no':
        continue_bidding = False
        get_highest_bidder(bidders)
    elif con == "yes":
        
        clear_console()
    



    


