
<!--PROJECT LOGO #will add later
<br />
<p align="center">
  <a href="https://github.com/campusrover/UntouchableHopscotchGame">
    <img src="images/logo.png" alt="Logo" width="80" height="80">
  </a> -->

  <h3 align="center">Untouchable Hopscotch by Al Colon</h3>

  <p align="center">
    A game brimming with anticipation, fear and excitement. Race against a CPU as you try to reach the treasure at the end of a long, grueling, and logic-defining journey. Can you beat Master CPU?
    <br />
    <a href="https://campusrover.github.io/UntouchableHopscotchGame"><strong>GitPages »</strong></a>
    <br />
    <br />
    <a href="https://youtu.be/6-SiT4fElZY">View Demo</a>
    ·
    <a href="https://github.com/campusrover/UntouchableHopscotchGame/issues">Report Bug</a>
    ·
    <a href="https://github.com/campusrover/UntouchableHopscotchGame/issues">Request Feature</a>
  </p>
</p>



<!-- TABLE OF CONTENTS -->
<details open="open">
  <summary><h2 style="display: inline-block">Table of Contents</h2></summary>
  <ol>
    <li>
      <a href="#about-the-project">About The Project</a>
      <ul>
        <li><a href="#built-with">Built With</a></li>
      </ul>
    </li>
    <li>
      <a href="#getting-started">Getting Started</a>
      <ul>
        <li><a href="#prerequisites">Prerequisites</a></li>
        <li><a href="#installation">Installation</a></li>
      </ul>
    </li>
    <li><a href="#how-to-play">How to Play</a></li>
   <li><a href="#contributing">Contributing</a></li>
    <li><a href="#license">License</a></li>
    <li><a href="#contact">Contact</a></li>
    <li><a href="#acknowledgements">Acknowledgements</a></li>
  </ol>
</details>



<!-- ABOUT THE PROJECT -->
## A note from the developer

Hi! Thanks for visiting my repo. I hope you have fun playing the game and playing with the code. I tried to make the code as modular as possible so I am excited to see if any ros developers would like to take a crack at customizing it. Enjoy!




### Built With

* [rospy](http://wiki.ros.org/rospy)
* [Open_CV](https://docs.opencv.org/master/)
* [Blender](https://docs.blender.org/)



<!-- GETTING STARTED -->
## Getting Started

To get a local copy up and running follow these simple steps.

### Prerequisites

You will need ROS, Gazebo and Python8

### Installation

1. Clone the repo inside catkin_ws you can use aldopkg or your own package
   ```sh
   git clone https://github.com/campusrover/UntouchableHopscotchGame.git
   ```

### Create new gameboards!
The original blender files for all the gameboards are also available! If you want to add more, change up the patterns, go nuts! I found that the dimensions 10mx10m was good for the turtlebots but feel free to adjust to your liking. You can refer to the [Lab Contribution](https://campus-rover.gitbook.io/lab-notebook/faq/diy-gazebo-world) for how to add your custom gameboard to Gazebo.

<!-- USAGE EXAMPLES -->
## How to Play
Follow these steps in order to play!
1. Launch the world
```
roslaunch aldopkg eightboard.launch # this will launch the board and robots
```
2. Start Game
```
rosrun aldopkg Game.py #this will launch the game node
```
3. Start CPU_Robot in a separate terminal
```
rosrun aldopkg CPU_robot.py #this will launch the cpu node
```
4. Start User_Robot in a separate terminal
```
rosrun aldopkg User_robot.py #this will launch the user node
```

Follow the instructions in the terminal and have fun!

## Entry in Lab Notebook about Creating Gazebo World

[Refer here for instruction on creating your own gameboard](https://campus-rover.gitbook.io/lab-notebook/faq/diy-gazebo-world)


<!-- LICENSE -->
## License

Distributed under the MIT License. See `LICENSE` for more information.

## Acknowlegements

Thank you 2021 Autonomous Robotics for such a fun and rewards class! Special thank you to Pito Salas and TAs August and Arjun for their help this semester.

<!-- CONTACT -->
## Contact

Al Colon - alexaleighcolon@gmail.com

Project Link: [https://github.com/campusrover/UntouchableHopscotchGame](https://github.com/campusrover/UntouchableHopscotchGame)
