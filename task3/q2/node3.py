import rclpy
from rclpy.node import Node
from std_msgs.msg import Int32
from taskone_interfaces.msg import RT2String


class ResultResponder(Node):
    def __init__(self):
        super().__init__('result_responder')

        self.publisher = self.create_publisher(
            RT2String, '/palindrome_response', 10
        )

        self.create_subscription(
            Int32, '/palindrome_result', self.send_response, 10
        )

    def send_response(self, msg):
        response = RT2String()
        response.data = "Yes" if msg.data == 1 else "No"

        self.publisher.publish(response)
        self.get_logger().info(f"Response: {response.data}")


def main(args=None):
    rclpy.init(args=args)
    node = ResultResponder()
    try:
        rclpy.spin(node)
    except KeyboardInterrupt:
        pass
    node.destroy_node()
    rclpy.shutdown()


if __name__ == '__main__':
    main()
