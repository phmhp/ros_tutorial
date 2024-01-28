#!/usr/bin/env python3
# -*- coding: utf-8 -*-
import rospy
import sys

from Message.msg import Message0, Message1, Message2
from std_msgs.msg import Int32

class Node2():

    def __init__(self):
        rospy.init_node('node2') #node name = node2
        arg = rospy.myargv(argv = sys.argv) #argument 
        rate = rospy.Rate(10)#1 seconde 10 roop 

        #message instance
        self.msg2 = Message2()
        self.msg1 = Message1()

        pub = rospy.Publisher("/node2_msg", Message2, queue_size=10) #publisher
        rospy.Subscriber("/node1_msg", Message1, self.from1_callback) #subscriber
      
        
        #run 
        while not rospy.is_shutdown():
            self.msg2.header.seq=0
            self.msg2.header.stamp = rospy.Time.now()
            self.msg2.header.frame_id="frame_id"

            #self.from1_callback(self.msg1)

            pub.publish(self.msg2)
            rate.sleep()


    
    def from1_callback(self,data):
        self.msg1 = Message1()
        self.msg1 = data
        self.msg2.frandom2 = self.msg1.from0 * 0.1

    
if __name__ == '__main__':
    try:
        node2 = Node2()
    except rospy.ROSInterruptException:
        pass