#!/usr/bin/env python

#######################
#title: door open
#author: Koya Okuse
#data: 2021/07/18
#######################

import rospy
from sensor_msgs.msg import LaserScan
from geometry_msgs.msg import Twist

class SubscriberClass():
    def __init__(self):
        self.ranges_message = rospy.Subscriber('/scan' , LaserScan, self.message_CallBack)
        self.laser = LaserScan()

    def message_CallBack(self, receive_msg):
        self.laser = receive_msg

    def message_value(self):
        if bool(self.laser.ranges):
            value = self.laser.ranges[359]
            print 'value'
            return value

class PublisherClass():

    def __init__(self):
        self.pub_message = rospy.Publisher('cmd_vel_mux/input/teleope', Twist,queue_size = 1)

    def lineContorol(self, value):
        twist_cmd = Twist()
        twist_cmd.linear.x = value
        rospy.sleep(0.1)
        self.pub_message.publish(twist_cmd)

def main():
    safety_distance = 2.0
    rospy.loginfo('start "open door"')
    sub = SubscriberClass()
    pub = PublisherClass()
    while not rospy.is_shutdown():
        state = sub.message_value()
        if state >= safety_distance:
            rospy.loginfo('start forward')
            pub.lineContorol(0.2)
        else:
            pass

if __name__ == '__main__':
    rospy.init_node('door_open')
    main()
