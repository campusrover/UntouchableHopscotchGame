## Project Report
# UntouchableHopscotch
### by Al Colon

## Introduction

### Original Proposal

Originally based off of the Don't Touch the White Tile game that was popular in the early 2010s, UntouchableHopscotch was originally going to incorporate changing tiles in a 3x3, 4x4, and 8x8 gameboard. It was up to the computer to figure out how to get to it's goal tile through OpenCV, restricted by its designated color. While it would have been cool to get the tiles to change colors. I was afraid that figuring out how to get the tiles to shift would take too much time. I also wanted to incorporate a teleop robot that would let the user race against the robot. This would make the game more immersive and playable. Both player would essentially have four movement options

### My Answer/Where it ended up

The general idea has stayed the same but there have been a lot of under the hood tweaks. While I did not have the changing color tiles, I implemented a timed color change which essentially did the same thing. By introducing a game node that is responsible for reporting what color each robot can and cannot use. This leaves more computing space for each robot, especially for the CPU robot.

#### CPU
The CPU robot is the most involved part of my project coding-wise. This robot starts off knowing its (x,y) location, the (x,y) location of the goal piece and what color it can use. It starts off with black but it will change as the game node sees fit.
Originally, it would have been able to go black and to the left. However, I realized that it made more sense to consider that the robot would be better off just waiting for the colors to change if it got stuck. This greatly streamlined the algorithm as it only had three decision to make.

What I have now is an autonomous robot that can 


## Relevant Literature

## What was Created
### What is UntouchableHopscotch
### How to play
### Process of creating the game
### Problems along the Way
### Solutions and Pivots

## Reflection
### Working with Harris and Jacqueline
### Leaving to Work Solo
### Working by Myself


- Bulleted
- List

1. Numbered
2. List

**Bold** and _Italic_ and `Code` text

[Link](url) and ![Image](src)
```
