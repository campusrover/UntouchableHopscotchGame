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

#### GAME
Developments regarding the game are none too few. While the core function of the game manager stayed mostly the same, the features that I wanted to include mostly has to do with different mode for play was completely abandoned. While it would have been cool to see the gamemode change, I simply ran out of time. It still will keep track of the bots and inform the of pertinent information, as seen in the STATS section, but that functionality will have to be included in a different iteration.

## Relevant Literature

- OpenCV
- Blender
- Gazebo Models

## What was Created

### What is UntouchableHopscotch

UntouchableHopscotch is a simple game. Both players are racing against each other to reach the goal tile and whoever gets there first wins. Each player is bounded to their designated color until the game node switches them and can only got up the board or to the right in relation to the board.

### How to play
Both players start inside the starting tile. CPU will be able to go on black tiles while User can go on white tiles.

Aimed towards the tile to which they have access, players can traverse their tiles upon go. CPU will start automatically, following its own algorithm, and user can follow the onscreen commands for going up and to the right, "w" and "d". Following the acceptable tiles, both bots will race to reach the yellow goal tile. Once one of the robots is on the tile, the game is over. The game will reset.

Although the robots will return to their location, game data will continue to be collected for previous wins and rounds.

### Stats
Stats and Info provided by the game include:
*Offered at the start*

- Friendly introduction
- Rules of the game
- Teleop instructions
- Restrictions

*Offered during*
- Color mode
- Color switch

*Offered After*
- Games played
- How many games won by user
- How many games won by cpu

Depending on the point of the game, different information will available to the user to help make it immersive.

### Process of creating the game
Because of the conditions of my assignment, I wanted to focus on synthesizing everything that we had used so far, in order to create a fully functioning project. This meant that I spent more time honing in on the specifics of topics that we had already covered rather the delve into something altogether new. Since I was creating a game, there was not a lot I could find to make it more interesting so I instead wanted to reallyy experiments with what I could do with what I had.

**Algorithms**
The automous robot in question is the CPU robot. With Open CV and ROS, the robot has to figure out the best path to the goal piece. It moves with a PID controller and "watches" its path to see if it is allowed to go that way. Since the goal piece could theoretically being anywhere, CPU will have to be viligilant about where it needs to go. It will know the location of the goal but the path is determined by how fast it responds to the color mode switch. It was interesting to me to see how the robot handles making decisons with simply noting a change in color. While my application of OpenCV was simple, understanding masks and color detection was a gateway to being able to explore topics outside of my project's own application such as face detection and real-time image analysis.

**Developing my own Gazebo World**
Nothing in this project made me wish I had a partner more than this aspect of the project. I spent way more time trying to figure out how to get gazebo to let me use my model. It ate up at least 40% of my development time. While the actual process of making my models was time-consuming as well, I knew that, at very least, once I was done, I could move on. I made many prototypes by only got to try out one because figuring out how to get a stable Gazebo world and roslaunch took me forever. Research was difficult because it seemed like no one had my exact problem. Implementing the solutions was even harder because it was difficult to tell whether the problem was the approach or the specifics. I made this my Lab Notebook Contribution with the hopes that no one else would be stuck on such a small aspect of a project. While I could get the robots to do what I want, it was essentially useless because I needed the model to tune the robots behavior. Even still, I learned a lot about the specifics of a physical world simulator and prototyping models through Gazebo.  The intimate understanding that I have of .sdf/.dae/.world files will be super helpful as I get into fields concerning design and prototyping. The hardware aspects might have scared me but getting to play settings in the virtual was very enlightening.

**Getting the robots to interact**
The robots may not have interacted physically but it did require some communication in order to get the robots to get some sense of place. To be honest, this was the most fun part of the project. I wanted to have a good user interface so that play was fairly intuitive. Granted, it is still limited to the terminal but it was fun to figure out how subscriber nodes could work to keep the bots and the user informed. I tried to create my own msgs but that just gave me more problems than I was ready to handle. The instructions I found for that both from the book and online did not work for me and learning from previous experiences with the 3d model import, if I am doing everything right and it is still not working, move right along. Another solution is probably right around the corner.



### Problems along the Way
To speak more specifically about the problems that I experienced, I think that because of the way I work and problem solve in general, I definitely could have benefitted from a new set of eyes when I encountered a new problem. As I mentioned before getting the model into the virtual space was the hardest and most time consuming aspect of my project. It got to the point that maybe I could instead simply try having an invisible board. One that the was communicated to the user and the cpu as a list. That solution was quickly abandoned as it would just be confusing and the user would be have no idea what was going on. Fortunately I got it work and was finally about to tune the board to work best.

I also wanted to work more with shape detection to help the robot calibrate but that didnt seem neccessary after watching it finally roll on the board.

As for the programming, aside from not being able to get msgs to work, there weren't really any problems that I didn't just need to debug. Again, I was working with mostly aspects of ROS that I already had encountered and due to timing was afraid that it would be better to get what I had going. This was unfortunate as it would have be very rewarding to learn how to apply a new brand new skill.

Before I switched to this project, I did have a chance to explore Fiducials with Jacqueline and Harris, however, while I still maintain a good understanding of how fiducials work, it was not relevant to my project.

### Solutions and Pivots
The biggest pivot I had to do was, of course, switching to a new project halfway in the semester. While I really liked working with the team I had, I simply did not want my mental health to affect their grade. I have not had a chance to talk to my former teammates about their progress without me but it seems as though they turned out alright. It was hard to tell if my output matched the teams but I think it worked out in the end.


## Reflection

### Working with Harris and Jacqueline

Since we did not have a lot of time to work together on the project, my reflection will be brief. I got a lot out of working with them but it was nice to be able to be more self-guided .As a team, it felt like we were pretty good at being self-guided. Splitting up the tasks was fairly easy. At the same time, with a deadline weeks away, the motivation to finish those tasks, dwindled. It was difficult to deal with new personalities and at times, it did feel like our project was dragging. I also was not able have much of a say on the project as it was for the greater good to agreed with the popular idea. There were moments of tension but it was good practice to have conversation about that tension and resolve any conflicts. I also did have a few moments of discomfort with these new personalities but as with life, it dealt with them appropriately and we were able to move on. While it was a personal experience that took me away from this group, it would have been a great project. With momentum picking towards the nend of the project, we had a good foundation to get the job done.

### Working by Myself
To say that creating this game was a huge challenge is an under statement. While I had the help of Arjun, I still felt lost for most of the assignment. While my plan was relatively easy, the lack of guidance outside of myself lead me to running into circles for most of the development. The concept was simple and I knew that steps to get to the finish-line was in my arsenal. I knew that there were definitely details that I needed to iron out but unfortunately, I underestimated how wrinkly my project was.

To my own fault, I had to relearn a lot of the basics because the application of them in my project required deeper understanding. Assumptions I had made about  ROS, lead to many moments of frustration. The solutions had seemed simple, however, as with life, that is rarely the case. Even though what I created wasn't too complicated, it took me forever to go through the trials and errors to get to where I am now. There was much that I learned in class and it only occured to me that most of what I accomplished was strictly self taught. There was no template for me to follow and it was up to me and me alone to understand what all this code meant. It was up to me to understand the specifics the programming. It was up to me to figure what I did wrong when the code refused to work. I felt guilty for how simple my assignment was but I felt like my own personal growth was huge. I came into this class not understanding a single word of Python or ROS but I still manage to get something working. From scratch, I was able to incorporate 3D modeling, ROS, Open CV all together to create a functional game.
## Links
[Lab Notebook Submission](https://campus-rover.gitbook.io/lab-notebook/faq/diy-gazebo-world)
[README.md](https://github.com/alcolon/UntouchableHopscotch#readme)

```
