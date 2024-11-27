'''The Travel Itinerary
Story: You are planning a trip and want to create an itinerary. You have a list of destinations, but they are all jumbled up. You want to print the destinations in alphabetical order so you can plan your trip better.

Problem: Write a Python program that takes a list of destinations and prints them in alphabetical order.

Example:

Input:
Paris Tokyo London NewYork

Output:
London NewYork Paris Tokyo'''

destination = input("Enter the name of destination:").lower().split()
sorted_destination = sorted(destination)
print(" ".join(sorted_destination))