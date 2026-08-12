import os
print("Welcome to the Secret Auction Program!")
bids = {}
while True:
    name = input("What is your name?: ")
    bid = int(input("What is your bid?: ₹"))
    bids[name] = bid
    another_bidder = input("Are there any other bidders? Type 'yes' or 'no'.\n")
    if another_bidder == "no":
        break
    os.system("cls" if os.name == "nt" else "clear")
highest_bid = 0
winner = ""
for name in bids:
    if bids[name] > highest_bid:
        highest_bid = bids[name]
        winner = name
print(f"The winner is {winner} with a bid of ₹{highest_bid}."   )
