'''Story: The town market is having a sale, and the shopkeeper wants to display the price tags in reverse order for some reason. The prices of the items are written in a single line, and you are tasked with reversing the digits of each price individually.

Problem: Write a Python program that reads a list of prices, reverses the digits of each price, and prints the reversed prices.

Example:

Input:
123 456 789

Output:
321 654 987'''

price_Tags = input("Enter Price Tags:")
prices = price_Tags.split()
for i in prices:
    reversed = [i[::-1]]
    print(" ".join(reversed),end=' ')    