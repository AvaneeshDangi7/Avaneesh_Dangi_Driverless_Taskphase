import rclpy
from rclpy.node import Node
from taskone_interfaces.msg import TaskOne


class WheelSubscriber(Node):
    def __init__(self):
        super().__init__('wheel_subscriber')
        self.subscription = self.create_subscription(
            TaskOne, '/taskone', self.calculate_speed, 10
        )

    def calculate_speed(self, msg):
        speed = msg.angVel * msg.radius
        self.get_logger().info(
            f"Longitudinal speed = {speed:.3f} m/s"
        )


def main(args=None):
    rclpy.init(args=args)
    node = WheelSubscriber()
    try:
        rclpy.spin(node)
    except KeyboardInterrupt:
        pass
    node.destroy_node()
    rclpy.shutdown()


if __name__ == '__main__':
    main()
