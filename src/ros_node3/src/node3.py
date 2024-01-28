#!/usr/bin/env python3
# -*- coding: utf-8 -*-

import rospy
import sys

from Message.msg import Message2
from std_msgs.msg import Int32

class Node3():

    def __init__(self):
        rospy.init_node('node3') #node name = node2
        arg = rospy.myargv(argv = sys.argv) #argument 
        rate = rospy.Rate(10)#1 seconde 10 roop 

        #message instance
        self.msg2 = Message2()
        self.msg3 = Message2()

        pub = rospy.Publisher("/node3_msg", Message2, queue_size=10) #publisher
        rospy.Subscriber("/node2_msg", Message2, self.from2_callback) #subscriber
      
        
        #run 
        while not rospy.is_shutdown():
            self.msg3.header.seq=0
            self.msg3.header.stamp = rospy.Time.now()
            self.msg3.header.frame_id="frame_id"

            self.from2_callback(self.msg2)

            pub.publish(self.msg3)
            rate.sleep()


    
    def from2_callback(self,data):
        self.msg2 = Message2()
        self.msg2 = data
        self.msg3.frandom3 = self.msg2.frandom2 * 1000

    
if __name__ == '__main__':
    try:
        node3 = Node3()
    except rospy.ROSInterruptException:
        pass