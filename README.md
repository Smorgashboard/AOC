ADVENT OF CODE 2024

A series of poorly optimized, badly written and half working solutions to the Advent of Code 2024

Day 1 : Easy. 

Day 2 : Had a harder time with getting a clean solution for checking the gradual report changes and direction of the changes when removing a single report value. I ended up with a brute force solution of just removing every value from the failed reports of the initial tests and then checking if it the reported values would pass the initial tests now.

Day 3 : Fun with Regex. I used chatgpt for the regex part. I also created a loop that could easily be infinite if the puzzle input was different, but it works fine for the puzzle input. Not optimized at all and a very ugly try/while loop but it was a long day at work and I wanted to keep up with the days.

Day 4 : Its hard to be this dumb.... I used numpy to make a grid and semi brute forced a solution by iterating through the grid and finding all the instances of X and then checking in every dircetion for M. If I found an M I checked for A in the same direction and if I found it I checked for an S. Part 1 was relatively easy all things considered. PT 2 was hell. It should have been easy to replicate my "brute forcing" and thats what i started with. I searched for an "A" and then checked each of the Diagonal directions for M or S and then inversed it to check for the opposite. If that completed I set a bool to true and executed the second check on the inverse of the original direction to check for M or S and again the opposite. It took me less than 30 minutes to write and 6-7 hours to find out that in my second checks I used the original direction instead of the new inverse direction. I am now 1 day behind. 
