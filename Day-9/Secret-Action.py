#Secret Action Programm
import os
from art import logo
print(logo)
print("Welcome to the secret auction program.")
is_bidding=True
bidder = {}

def highest_bidder(bidder_dist):
    winner = max(bidder_dist, key=bidder_dist.get)
    print(f"The winner is {winner} with a bid of ${bidder_dist[winner]}\n")


while is_bidding:
    name = input("What is your name?: ")
    bid = int(input("What's your bid?: $"))
    bidder[name]=bid
    repeat = input("Are there any other bidders? 'yes' or 'no'. ")
    os.system('cls')
    if repeat=='no':
        highest_bidder(bidder)
        is_bidding=False




    
