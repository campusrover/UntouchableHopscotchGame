#!/usr/bin/env python

import rospy
import sys
import math
import tf
from std_msgs.msg import String
from nav_msgs.msg import Odometry
from geometry_msgs.msg import Twist
from sensor_msgs.msg import LaserScan



# it is not necessary to add more code here but it could be useful
def key_cb(msg):
   global state
   state = msg.data




# init node
rospy.init_node('dancer')

# subscribers/publishers


# RUN rosrun prrexamples key_publisher.py to get /keys
key_sub = rospy.Subscriber('keys', String, key_cb)
color_sub = rospy.Subscriber ('/colormode', String, color_pub)
report_sub = rospy.Publisher()
cmd_vel_pub = rospy.Publisher('cmd_vel', Twist, queue_size=10)

# start in state halted and grab the current time
state = "H"
last_key_press_time = rospy.Time.now()

# set rate
rate = rospy.Rate(10)

# Wait for published topics, exit on ^c
while not rospy.is_shutdown():

   # print out the current state and time since last key press
   print_state()



   # run at 10hz
   rate.sleep()
