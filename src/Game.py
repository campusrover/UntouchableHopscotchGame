#!/usr/bin/env python
import rospy
from std_msgs.msg import String
# responsible for keeping track of player location and penalty

rospy.init_node('gamenode')

timer = 10 #secs
who_is_black = 0 # user is black

#Publishers
gamepub = rospy.Publisher('color_mode', String, queue_size=1)

#Subscribers
subcpu = rospy.Subscriber('/cpu_robot/odom', Odometry, cpu_odom_cb)
subuser = rospy.Subscriber('user_robot/odom', Odometry, user_odom_cb)

def cpu_odom_cb(msg):
    global cpu_x
    global cpu_y
    cpu_x = msg.data.pose.pose.position.x
    cpu_y = msg.data.pose.pose.position.y

def user_odom_cb(msg):
    global usr_x
    global usr_y
    usr_x = msg.data.pose.pose.position.x
    usr_y = msg.data.pose.pose.position.y

while (!rospy.is_shutdown):
    #text updated
