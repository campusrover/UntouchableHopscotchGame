#!/usr/bin/env python

import rospy
from std_msgs.msg import String
from geometry_msgs.msg import Twist

key_mapping = { 'w': [ 1, 0], 'x': [0, 0],
                'a': [0, 1], 'd': [0, -1],
            's':[-1, 0]} #values dedicated to which way the user would like to go
direct_mapping = {'w': "up", 'x': "stop"}
g_last_twist = None

# Default values for linear and angular. These will be multiplied by 1, 0 or -1
g_vel_scales = [0.1, 0.1] # default to very slow

def keys_cb(msg, twist_pub):


# Main program
if __name__ == '__main__':


    rospy.init_node('scarywasd')
    cv_pub = rospy.Publisher('cmd_vel', Twist, queue_size=1)

    # Declare subsription to keys topic
    rospy.Subscriber('keys', String, keys_cb, twist_pub)

    
    if ()
    x_old = x
    yaw_old = yaw
    target_rad = target_angle * math.pi/180
    while(yaw != 0):
        t.angular.z = kP  * (target_rad - yaw)
        cpub.publish(t)
    t.angular.z = 0
    cpub.publish(t)
    while (x - x_old <= distance_to_drive):
        t.linear.x = .3
        cpub.publish(t)
    t.linear.x =  0
    cpub.publish(t)
    location[0] += 1 # updating location

    # Publish whatever the current desired g_last_twist is
    while not rospy.is_shutdown():
        twist_pub.publish(g_last_twist)
        rate.sleep()
