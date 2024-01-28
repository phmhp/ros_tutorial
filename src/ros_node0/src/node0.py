#!/usr/bin/env python3
# -*- coding: utf-8 -*-
import rospy
import sys
import random

from Message.msg import Message0
from std_msgs.msg import Int32,Header 

class Node0():

    def __init__(self):
        rospy.init_node('node0')
        rate = rospy.Rate(10)

        self.msg0 = Message0()
        pub = rospy.Publisher("/node0_msg", Message0, queue_size=10)
        
        while not rospy.is_shutdown():
          
            self.msg0.header.seq = 0
            self.msg0.header.stamp = rospy.Time.now()
            self.msg0.header.frame_id = "frame_id" 
           
            self.msg0.random = random.randint(10,4294967295)

            pub.publish(self.msg0)
            rate.sleep()
        
if __name__ == '__main__':
    try:
        node0=Node0()
    except rospy.ROSInterruptException:
        pass
