## Project Report
# UntouchableHopscotch
### by Al Colon

## Introduction

### Original Proposal

Originally based off of the Don't Touch the White Tile game that was popular in the early 2010s, UntouchableHopscotch was originally going to incorporate changing tiles in a 3x3, 4x4, and 8x8 gameboard. It was up to the computer to figure out how to get to it's goal tile through OpenCV, restricted by its designated color. While it would have been cool to get the tiles to change colors. I was afraid that figuring out how to get the tiles to shift would take too much time. I also wanted to incorporate a teleop robot that would let the user race against the robot. This would make the game more immersive and playable.

I wanted to find a way to use the skills I learned in this class in a way that was fun for me and the user. While I was excited to learn how robots worked and the cool applications they have, I was more interested in how they could be used to simply entertain. With this project, I hoped to find a middle ground for technical application and practical application.

### My Answer/Where it ended up

The general idea has stayed the same but there have been a lot of under the hood tweaks. While I did not have the changing color tiles, I implemented a timed color change which essentially did the same thing. By introducing a game node that is responsible for reporting what color each robot can and cannot use. This leaves more computing space for each robot, especially for the CPU robot.

#### CPU
The CPU robot is the most involved part of my project coding-wise. This robot starts off knowing its (x,y) location, the (x,y) location of the goal piece and what color it can use. It starts off with black but it will change as the game node sees fit.
Originally, it would have been able to go black and to the left. However, I realized that it made more sense to consider that the robot would be better off just waiting for the colors to change if it got stuck. This greatly streamlined the algorithm as it only had three decision to make.

#### USER
Where the CPU got simpler, the user robot got a tad more complicated. It was always known that the robot would be operate with teleop but I thought it would be more convenient for the user if the wasd functions where mapped to the gameboard itself. This would mean that it would be easier for the user to navigate the gameboard.

## Relevant Literature

-OpenCV
## Project Report
# UntouchableHopscotch
### by Al Colon

## Introduction

### Original Proposal

Originally based off of the Don't Touch the White Tile game that was popular in the early 2010s, UntouchableHopscotch was originally going to incorporate changing tiles in a 3x3, 4x4, and 8x8 gameboard. It was up to the computer to figure out how to get to it's goal tile through OpenCV, restricted by its designated color. While it would have been cool to get the tiles to change colors. I was afraid that figuring out how to get the tiles to shift would take too much time. I also wanted to incorporate a teleop robot that would let the user race against the robot. This would make the game more immersive and playable.

I wanted to find a way to use the skills I learned in this class in a way that was fun for me and the user. While I was excited to learn how robots worked and the cool applications they have, I was more interested in how they could be used to simply entertain. With this project, I hoped to find a middle ground for technical application and practical application.

### My Answer/Where it ended up

The general idea has stayed the same but there have been a lot of under the hood tweaks. While I did not have the changing color tiles, I implemented a timed color change which essentially did the same thing. By introducing a game node that is responsible for reporting what color each robot can and cannot use. This leaves more computing space for each robot, especially for the CPU robot.

#### CPU
The CPU robot is the most involved part of my project coding-wise. This robot starts off knowing its (x,y) location, the (x,y) location of the goal piece and what color it can use. It starts off with black but it will change as the game node sees fit.
Originally, it would have been able to go black and to the left. However, I realized that it made more sense to consider that the robot would be better off just waiting for the colors to change if it got stuck. This greatly streamlined the algorithm as it only had three decision to make.

#### USER
Where the CPU got simpler, the user robot got a tad more complicated. It was always known that the robot would be operate with teleop but I thought it would be more convenient for the user if the wasd functions where mapped to the gameboard itself. This would mean that it would be easier for the user to navigate the gameboard.

## Relevant Literature

-OpenCV


## What was Created

### What is UntouchableHopscotch

UntouchableHopscotch is a simple game. Both players are racing against each other to reach the goal tile and whoever gets there first wins. Each player is bounded to their designated color until the game node switches them and can only got up the board or to the right in relation to the board.

### How to play
Both players start inside the starting tile. CPU will be able to go on black tiles while User can go on white tiles.

Aimed towards the tile to which they have access, players can traverse their tiles upon go. CPU will start automatically and user can follow the onscreen commands for going up and to the right.

### Stats

Stats available from
### Process of creating the game
### Problems along the Way
### Solutions and Pivots

## Reflection
### Working with Harris and Jacqueline
### Leaving to Work Solo
### Working by Myself

## Links
[Lab Notebook Submission](https://campus-rover.gitbook.io/lab-notebook/faq/diy-gazebo-world)
[README.md](https://github.com/alcolon/UntouchableHopscotch#readme)




## What was Created
### What is UntouchableHopscotch
UntouchableHopscotch is a simple game. Both players are racing against each other to reach the goal tile and whoever gets there first wins. Each player is bounded to their designated color until the game node switches them and can only got up the board or to the right in relation to the board.
### How to play
Both players start inside the starting tile. CPU will be able to go on black tiles while User can go on white tiles.

Aimed towards the tile to which they have access, players can traverse their tiles upon go.
### Stats
Stats will include
### Process of creating the game
### Problems along the Way
### Solutions and Pivots

## Reflection
### Working with Harris and Jacqueline
### Leaving to Work Solo
### Working by Myself
