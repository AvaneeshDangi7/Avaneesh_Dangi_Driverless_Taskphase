import rclpy
from rclpy.node import Node
from taskone_interfaces.msg import RT2String


class StringPublisher(Node):
    def __init__(self):
        super().__init__('string_publisher')
        self.publisher = self.create_publisher(
            RT2String, '/rt2_string', 10
        )
        self.timer = self.create_timer(1.0, self.publish_string)

    def publish_string(self):
        text = input("Enter a string (or quit): ")

        if text.lower() == 'quit':
            raise KeyboardInterrupt

        msg = RT2String()
        msg.data = text
        self.publisher.publish(msg)
        self.get_logger().info(f"Published: {text}")


def main(args=None):
    rclpy.init(args=args)
    node = StringPublisher()
    try:
        rclpy.spin(node)
    except KeyboardInterrupt:
        pass
    node.destroy_node()
    rclpy.shutdown()


if __name__ == '__main__':
    main()
