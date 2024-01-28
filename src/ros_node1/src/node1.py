#!/usr/bin/env python3
# -*- coding: utf-8 -*-
import rospy
import sys

from message.msg import Message0, Message1, Message3
from std_msgs.msg import Int32

class Node1():

    def __init__(self):
        rospy.init_node('node1') #node name = node1 
        arg = rospy.myargv(argv = sys.argv) #argument 
        rate = rospy.Rate(10)#1 seconde 10 roop 

        #message instance
        self.msg0 = Message0()
        self.msg3 = Message3()
        self.msg1 = Message1()

        pub = rospy.Publisher("/node1_msg", Message1, queue_size=10) #publisher
        rospy.Subscriber("/node0_msg", Message0, self.from0_callback) #subscriber
        rospy.Subscriber("/node3_msg", Message3, self.from3_callback) #subscriber 
        
        #run 
        while not rospy.is_shutdown():
            msg1.header.seq=0
            msg1.header.stamp = rospy.Time.now()
            msg1.header.frame_id="frame1"
            msg1.random = random.()
            msg1.from0 = msg0+3
            msg1.from3 = msg3 / 10
			pub.publish(self.msg1)
            rate.sleep()


    
    def from0_callback(self,data):
        self.msg0 = Message0()
        self.msg0 = data

    def from3_callback(self,data3):
        self.msg3 = Message3()
        self.msg3 = data3
    

    
if __name__ == '__main__':
    try:
        node1 = Node1()
    except rospy.ROSInterruptException:
        pass