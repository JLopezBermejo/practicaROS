#!/usr/bin/env python3
import time

import rclpy
from rclpy.node import Node
from std_msgs.msg import Char
from geometry_msgs.msg import Twist



class NodoSuscriptor(Node):
    def __init__(self, name):
        super().__init__(name)
        self.suscriber = self.create_subscription(
            Char, "/charstream", self.callback, 10)

    def callback(self, msg):
        vector = Twist()
        if msg.data == ord('w'):
            vector.linear.y = 1.0
            self.create_publisher(Twist, "/turtle1/cmd_vel", 10).publish(vector)
        elif msg.data == ord('a'):
            vector.linear.x = -1.0
            self.create_publisher(Twist, "/turtle1/cmd_vel", 10).publish(vector)
        elif msg.data == ord('s'):
            vector.linear.y = -1.0
            self.create_publisher(Twist, "/turtle1/cmd_vel", 10).publish(vector)
        elif msg.data == ord('d'):
            vector.linear.x = 1.0
            self.create_publisher(Twist, "/turtle1/cmd_vel", 10).publish(vector)


def main(args=None):
    try:
        print("Aplicacion iniciada")
        rclpy.init(args=args)
        nodeSuscriptor = NodoSuscriptor('suscriptor')
        rclpy.spin(nodeSuscriptor)
    finally:
        rclpy.shutdown()


if __name__ == '__main__':
    main()
