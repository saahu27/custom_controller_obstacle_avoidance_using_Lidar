#! /usr/bin/env python
import rospy

from sensor_msgs.msg import LaserScan

def callback(msg):
    print(len(msg.ranges))

def main():

    rospy.init_node('scan_values')

    sub = rospy.Subscriber('/scan', LaserScan, callback)
    rospy.spin()
    
if __name__ == '__main__':
    main()
