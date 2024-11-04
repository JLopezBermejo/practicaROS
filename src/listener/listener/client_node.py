#!/usr/bin/env python3
import time

import rclpy
from rclpy.node import Node
from turtlesim.srv import TeleportAbsolute
from functools import partial
from std_msgs.msg import Char


class ResetNodeCliente(Node):
    def __init__(self):
        super().__init__('cliente')
        self.suscriber = self.create_subscription(
            Char, "/charstream", self.callback, 10)

    def callback(self, msg):
        client = self.create_client(TeleportAbsolute, '/turtle1/teleport_absolute')
        while not client.wait_for_service(1.0):
            self.get_logger().info("esperando a enviar")
        if msg.data == ord('r'):
            request = TeleportAbsolute.Request()
            request.y = 5.54444456
            request.x = 5.54444456
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
        nodoCliente = ResetNodeCliente()
        rclpy.spin(nodoCliente)
    finally:
        rclpy.shutdown()


if __name__ == '__main__':
    main()
