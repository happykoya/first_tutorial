#!/usr/bin/env python
import rospy
import time
from geometry_msgs.msg import Twist

class Test():
    def __init__(self):
        self.pub = rospy.Publisher('cmd_vel_mux/input/teleope', Twist, queue_size=1)


    def pub_x(self):

        dist = 1.0
        speed = 0.2
        target_time = dist / speed


        t = Twist()
        t.linear.x = speed
        t.angular.z = 0


        start_time = time.time()
        #
        end_time = time.time()

        #
        rate = rospy.Rate(30)
        while end_time - start_time <= target_time:
            self.pub.publish(t)
            end_time = time.time()
            rate.sleep()

    #
    def pub_z(self):
        #
        theta = 180.0 # [deg]
        speed = 90.0 # [deg/s]
        target_time = theta / speed # [s]

        #
        t = Twist()
        t.linear.x = 0
        t.angular.z = speed * 3.1415 / 180.0 # [rad]

        #
        start_time = time.time()
        #
        end_time = time.time()

        rate = rospy.Rate(30)
        while end_time - start_time <= target_time:
            self.pub.publish(t)
            end_time = time.time()
            rate.sleep()

if __name__ == '__main__':
    rospy.init_node('tcmdvel_publisher')
    test = Test()

    test.pub_x()
    
    test.pub_z()
