#! /usr/bin/env python

import rospy

from sensor_msgs.msg import LaserScan
from geometry_msgs.msg import Twist
pub = None

move = Twist()

def clbk_laser(msg):
    linear_x = 0
    angular_z = 0
    count = 0
    sum = 0
    laser = list()
    #laser60,laser90,laser120,laser150,laser180,laser210,laser240,laser270,laser300,laser330,laser360 = 0
    for i in range(0,360):

        sum = sum + msg.ranges[i]
        count +=1

        if(count == 30):
            laser.append(sum/30)
            sum = 0
        if(count == 60):
            laser.append(sum/30)
            sum = 0

        if(count == 90):
            laser.append(sum/30)
            sum = 0

        if(count == 120):
            laser.append(sum/30)
            sum = 0

        if(count == 150):
            laser.append(sum/30)
            sum = 0

        if(count == 180):
            laser.append(sum/30)
            sum = 0

        if(count == 210):
            laser.append(sum/30)
            sum = 0
        if(count == 240):
            laser.append(sum/30)
            sum = 0
        if(count == 270):
            laser.append(sum/30)
            sum = 0
        if(count == 300):
            laser.append(sum/30)
            sum = 0
        if(count == 330):
            laser.append(sum/30)
            sum = 0
        if(count == 360):
            laser.append(sum/30)
            sum = 0

    zerotoleft = (laser[0] + laser[1])/2
    left = (laser[2] + laser[3])/2
    behind = (laser[4] + laser[5] + laser[6] + laser[7])/4
    right = (laser[8] + laser[9])/2
    righttozero = (laser[10] + laser[11])/2

    if zerotoleft > 1 and righttozero > 1 :
        print('case 1-No obstacle infront')
        linear_x = 0.5
        angular_z = 0
    elif zerotoleft > 1 and righttozero < 1 :
        if left > right :
            print('case 2- going left,No obstacle on the zerotoleft and left,obstacle in righttozero')
            linear_x = 0
            angular_z = 0.4
        elif right > left :
            print('case 3 - going right,no obstacle on the zerotoleft and right,obstacle in left')
            linear_x = 0
            angular_z = -0.4
        elif right == left :
            linear_x = 0
            angular_z = 0.5

    elif zerotoleft < 1 and righttozero > 1 :
        if right > left :
            print('case 4 - going right, obstacle in the zerotoleft,righttozero')
            linear_x = 0
            angular_z = -0.4
        elif left> right:
            print('case 5 - going left,o obstacle on the zerotoleft and right')
            linear_x = 0
            angular_z = 0.4
        elif right == left :
            linear_x = 0
            angular_z = 0.5
    
    elif zerotoleft < 1 and righttozero <1:
        if right > left :
            print('case 6 - going right, obstacle in the zerotoleft,righttozero')
            linear_x = 0
            angular_z = -0.4
        elif left> right:
            print('case 7 - going left,o obstacle on the zerotoleft and right')
            linear_x = 0
            angular_z = 0.4
        elif right == left :
            linear_x = 0
            angular_z = 0.5
    else:
        print("unkown condition")
        rospy.loginfo(laser)

    move.linear.x = linear_x
    move.angular.z = angular_z

    pub.publish(move)

def main():
    global pub
    
    rospy.init_node('reading_laser')
    
    pub = rospy.Publisher('/cmd_vel', Twist, queue_size=1)
    
    sub = rospy.Subscriber('/scan', LaserScan, clbk_laser)
    
    rospy.spin()

if __name__ == '__main__':
    main()
