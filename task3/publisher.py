import rclpy
from rclpy.node import Node
from taskone_interfaces.msg import TaskOne


class WheelPublisher(Node):
    def __init__(self):
        super().__init__('wheel_publisher')
        self.publisher = self.create_publisher(
            TaskOne, '/taskone', 10
        )
        self.timer = self.create_timer(1.0, self.publish_data)

    def publish_data(self):
        try:
            ang_vel = float(input("Enter angular velocity (rad/s): "))
            radius = float(input("Enter wheel radius (m): "))

            msg = TaskOne()
            msg.angvel = ang_vel
            msg.radius = radius

            self.publisher.publish(msg)
            self.get_logger().info(
                f"Published angvel={ang_vel}, radius={radius}"
            )
        except ValueError:
            self.get_logger().error("Enter valid numeric values.")


def main(args=None):
    rclpy.init(args=args)
    node = WheelPublisher()
    try:
        rclpy.spin(node)
    except KeyboardInterrupt:
        pass
    node.destroy_node()
    rclpy.shutdown()


if __name__ == '__main__':
    main()
