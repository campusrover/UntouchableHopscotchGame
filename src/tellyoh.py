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
    global g_last_twist, g_vel_scales

    # Allow for blank data from keys topic, or a key that has no mapping
    if len(msg.data) == 0 or not key_mapping.has_key(msg.data[0]):
        return # unknown key

    # Based on key grab 0, 1 or -1 for linear and angular
    vels = key_mapping[msg.data[0]]

    # Multiply multiplier by absolute value in g_vel_scales
    g_last_twist.angular.z = vels[0] * g_vel_scales[0]
    g_last_twist.linear.x = vels[1] * g_vel_scales[1]

    # And publish cmd_vel
    twist_pub.publish(g_last_twist)

# Main program
if __name__ == '__main__':

    # Declare node-hood
    rospy.init_node('keys_to_twist')

    # Declare that want to publish cmd_vel
    twist_pub = rospy.Publisher('cmd_vel', Twist, queue_size=1)

    # Declare subsription to keys topic
    rospy.Subscriber('keys', String, keys_cb, twist_pub)

    # Create a blank twist
    g_last_twist = Twist() # initializes to zero

    # Based on param either on command line, grab the absolute values for linear and angular
    #moves into next box
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
