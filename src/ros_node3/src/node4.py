#!/usr/bin/env python3
# -*- coding: utf-8 -*-

import rospy
import sys

from Message.msg import Message2
from std_msgs.msg import Int32

class Node4():

    def __init__(self):
        rospy.init_node('node4') #node name = node4
        arg = rospy.myargv(argv = sys.argv) #argument 
        rate = rospy.Rate(10)#1 seconde 10 roop 

        #message instance
        self.msg2 = Message2()
        self.msg4 = Message2()

        rospy.Subscriber("/node2_msg", Message2, self.from2_callback) #subscriber
      
        
        #run 
        while not rospy.is_shutdown():
            self.msg4.header.seq=0
            self.msg4.header.stamp = rospy.Time.now()
            self.msg4.header.frame_id="frame_id"

            self.from2_callback(self.msg2)

            rate.sleep()


    
    def from2_callback(self,data):
        self.msg2 = Message2()
        self.msg2 = data
        self.msg4.frandom3 = self.msg2.frandom2 * 1000

    
if __name__ == '__main__':
    try:
        node4 = Node4()
    except rospy.ROSInterruptException:
        pass