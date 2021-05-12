#!/usr/bin/env python

import rospy, cv2, cv_bridge, numpy, math, imutils
from geometry_msgs.msg import Twist
from nav_msgs.msg import Odometry
from std_msgs.msg import Int32
from sensor_msgs.msg import Image
from tf.transformations import euler_from_quaternion
from scipy.spatial import distance
from collections import OrderedDict

class CPU:
    def __init__(self):
        ###############Publishers#################
        #pubs
        self.bridge = cv_bridge.CvBridge()
        self.move = rospy.Publisher('/cpu/cmd_vel', Twist, queue_size=1)

        #subs
        self.cpsub = rospy.Subscriber('cpu/odom', Odometry, self.odom_cb)
        self.color = rospy.Subscriber('color_mode', Int32, self.color_cb)
        #self.status = rospy.Subscriber('winner', Int32, self.status_cb)
        self.goal = rospy.Subscriber('goal', Int32, self.goal_tile)
        self.eyes = rospy.Subscriber('/cpu/camera/rgb/image_raw', Image, self.image_callback)


        #variables
        self.goal = [0,0]
        self.location = [0,0]
        self.permission = False # tells the robot if it can go on a tile
        self.nextStep = ""
        self.color = ""
        self.setting = "black"
        self.direction = 0 # right
        self.status = 0

        self.kp = .5
        self.d = rospy.Duration.from_sec(10)


        self.colors = OrderedDict({ "black" : (0, 0, 0),
                                    "white" : (255, 255, 255)})

        self.rate = rospy.Rate(10)
        self.gas_pedal = Twist()

        self.lab = numpy.zeros((len(self.colors), 1, 3), dtype="uint8")

        self.colornames = []

        for (i, (name, rgb)) in enumerate(self.colors.items()):
            self.lab[i] = rgb
            self.colornames.append(name)

        self.lab = cv2.cvtColor(self.lab, cv2.COLOR_BGR2LAB)

    def image_callback(self, msg):
        self.image = self.bridge.imgmsg_to_cv2(msg)
        self.imgblur = cv2.GaussianBlur(self.image, (7,7), 1)
        self.gray = cv2.cvtColor(self.imgblur, cv2.COLOR_BGR2GRAY)
        cv2.imshow('original', self.image)


    # creates tunnel vision
        self.blank = numpy.zeros(self.image.shape[:2], dtype='uint8')
        mask = cv2.circle(self.blank, (1000,800), 25, 255, -1)
        masked = cv2.bitwise_and(self.image, self.image, mask=mask)
        cv2.imshow('eye', masked)


    #creating contour
        self.edge = cv2.Canny(masked, 75, 200)
        cv2.imshow('contour', self.edge)

        _, contours, _ = cv2.findContours(self.edge, cv2.RETR_TREE, cv2.CHAIN_APPROX_SIMPLE)

        contour_list = []
        for contour in contours:
            self.approx = cv2.approxPolyDP(contour,0.01*cv2.arcLength(contour,True),True)
            self.area = cv2.contourArea(contour)
            if ((len(self.approx) > 8) & (len(self.approx) < 23) & (self.area > 30) ):
                contour_list.append(contour)

        mask = numpy.zeros(self.image.shape[:2], dtype="uint8")
        cv2.drawContours(mask, contour_list, 0, 255, -1)
        mask = cv2.erode(mask, None, iterations=2)
        mean = cv2.mean(self.image, mask=mask)[:3]

        #detecting color
        minDis = (numpy.inf, None)

        for (i, row) in enumerate(self.lab):
            d = distance.euclidean(row[0], mean)

            if d < minDis[0]:
                minDis = (d, i)


        self.nextStep = self.colornames[minDis[1]]
        if (self.nextStep == self.setting):
            self.permission = True
        else:
            self.permission = False
        print(str(self.colornames[minDis[1]]))

        cv2.waitKey(3)


    def goal_tile(msg):
            self.goal = msg.data

    def odom_cb(self,msg):
        self.x = msg.pose.pose.position.x
        self.y = msg.pose.pose.position.y

        self.orientation_q = msg.pose.pose.orientation
        self.orientation_list = [self.orientation_q.x, self.orientation_q.y, self.orientation_q.z, self.orientation_q.w]
        (self.roll, self.pitch, self.yaw) = euler_from_quaternion (self.orientation_list)

    # tells the robot what color it can go on
    def color_cb(self, msg):
        self.setting = msg.data  # 0 is black, 1 is white
        if self.setting == 0:
            self.color = "black"
        else:
            self.color = "white"

    # status of game
    def status_cb(self, msg):

        self.leaderboard = msg.data

        if (self.status == 0): # no one has won
            self.game_on()
        else:
            if (self.status == 1): #cpu has won
                self.happydance()
            stop()


        # -----------------DIRECTIONS-----------------------------



    while (True):
        if (permission):
            self.drive()
        else:
            if (direction == 0):
                self.up()
                self.direction = 1
            else:
                self.right()
                self.direction = 0


    def up(): #moves into next box
        now = rospy.get_rostime()
        stop = self.d + now
        while (rospy.get_rostime() < stop):
            target_rad = 0
            gas_pedal.angular.z = .5 * (target_rad-self.yaw)
            move.publish(gas_pedal)


    def right():
        now = rospy.get_rostime()
        stop = self.d + now
        while (rospy.get_rostime() < stop):
            target_rad = -1.57
            move.angular.z = .5 * (target_rad-self.yaw)
            move.publish(t)


    def stop():
        while(true):
            self.gas_pedal.angular.z = 0
            self.gas_pedal.linear.x = 0
            self.publish(gas_pedal)

    def drive():
        gas_pedal.angular.z = 0
        gas_pedal.linear.x = .2
        move.publish(gas_pedal)
        rospy.sleep(5)
        gas_pedal.linear.x = 0
        move.publish(gas_pedal)
        rospy.sleep(5)

    def happy_dance():
        self.gas_pedal.angular.z = 2 #meters
        self.move.publish(t)
        self.timebuffer()
        self.stop()


    def where_am_i():
        print(str(location))


# set up nodes
rospy.init_node('cpu')
cpu = CPU()
rospy.spin()
