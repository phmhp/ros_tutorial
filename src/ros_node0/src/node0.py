#!/usr/bin/env python3
# -*- coding: utf-8 -*-
import rospy
import sys
import random

from message.msg import Message0  # 수정된 부분
from std_msgs.msg import Int32, Header

class Node0():

    def __init__(self):
        rospy.init_node('node0')
        rate = rospy.Rate(10)
        self.msg0 = Message0()  # 수정된 부분

        pub = rospy.Publisher("/node0_msg", Message0, queue_size=10)
        
        while not rospy.is_shutdown():
          
            self.msg0.header.stamp = rospy.Time.now()  # 수정된 부분
            self.msg0.header.seq = 0
            self.msg0.header.frame_id = "frame1" 
           
            self.msg0.random = random.randint(10, sys.maxsize)  # 수정된 부분

            pub.publish(self.msg0)
            rate.sleep()
        
if __name__ == '__main__':
    try:
        node0 = Node0()
    except rospy.ROSInterruptException:
        pass

