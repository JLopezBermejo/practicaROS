#!/usr/bin/env python3
import time

import rclpy
from rclpy.node import Node
from turtlesim.srv import SetPen
from functools import partial
from std_msgs.msg import Char


class ClearNodeCliente(Node):
    def __init__(self):
        super().__init__('cliente')
        self.on_off = False
        self.suscriber = self.create_subscription(
            Char, "/charstream", self.callback, 10)

    def callback(self, msg):
        client = self.create_client(SetPen, '/turtle1/set_pen')
        while not client.wait_for_service(1.0):
            self.get_logger().info("esperando a enviar")
        if msg.data == ord(' '):
            request = SetPen.Request()
            request.off = not self.on_off
            request.b = 255
            request.g = 184
            request.r = 179
            request.width = 3
            self.on_off = not self.on_off
            future = client.call_async(request)
            future.add_done_callback(partial(self.callback_con_respuesta))

    def callback_con_respuesta(self, future):
        try:
            response = future.result()
        except Exception as e:
            self.get_logger().error(e)

def main(args=None):
    try:
        print("Aplicacion iniciada")
        rclpy.init(args=args)
        nodoCliente = ClearNodeCliente()
        rclpy.spin(nodoCliente)
    finally:
        rclpy.shutdown()


if __name__ == '__main__':
    main()
