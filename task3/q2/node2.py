import rclpy
from rclpy.node import Node
from taskone_interfaces.msg import RT2String
from std_msgs.msg import Int32


class PalindromeChecker(Node):
    def __init__(self):
        super().__init__('palindrome_checker')

        self.result_pub = self.create_publisher(
            Int32, '/palindrome_result', 10
        )

        self.create_subscription(
            RT2String, '/rt2_string', self.check_palindrome, 10
        )

        self.create_subscription(
            RT2String, '/palindrome_response', self.receive_response, 10
        )

    def check_palindrome(self, msg):
        text = msg.data
        result = Int32()
        result.data = int(text == text[::-1])

        self.result_pub.publish(result)

        self.get_logger().info(
            f"Input: {text}, palindrome result: {result.data}"
        )

    def receive_response(self, msg):
        self.get_logger().info(f"Response from Node 3: {msg.data}")


def main(args=None):
    rclpy.init(args=args)
    node = PalindromeChecker()
    try:
        rclpy.spin(node)
    except KeyboardInterrupt:
        pass
    node.destroy_node()
    rclpy.shutdown()


if __name__ == '__main__':
    main()
