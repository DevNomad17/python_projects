import common

print(common.art_auction)
print("Welcome to the secret auction program.")

next_bidder = "yes"
bids = {}

while next_bidder == "yes":
    name = input("What is your name?: ")
    bid = int(input("What's your bid?: $"))
    next_bidder = input("Are there any other bidders? Type 'yes' or 'no': ")
    print("\n\n\n\n\n\n\n\n\n\n\n\n\n\n")
    bids[name] = bid

winner_name = ""
winner_bid = 0

for bid in bids:
    if bids[bid] > winner_bid:
        winner_bid = bids[bid]
        winner_name = bid

print(f"The winner is {winner_name} with a bid of ${winner_bid}")



