#!/usr/bin/env python
#-*- coding:utf-8 -*-
#--------------------------------------
#Title:ROs Nodeを理解するためのサンプルコード
#Author:Koya Okuse
#Date:2021/07/13
#Memo:１秒おきに世界に挨拶するプログラム
#       Ctrl +C 押されたら別れを告げる
#-------------------------------------
import rospy
a = 0
def main():
    count = 1
    count_h = 1
    while not rospy.is_shutdown():

        rospy.loginfo('Hello World')
        for count_h in range(count):
             print('Hello World' + str(count_h))
             rospy.sleep(1.0)
        count += 1
    rospy.loginfo('Good bye')

if __name__== '__main__':
    rospy.init_node('tuto_node',anonymous = True)
    main()
