import rclpy
from rclpy.node import Node
from geometry_msgs.msg import Pose
import math
import random

class SensorPublisher(Node):
    def __init__(self):
        super().__init__('sensor_publisher')
        self.publisher_ = self.create_publisher(Pose, 'sensor_data', 10)
        self.timer = self.create_timer(0.5, self.publish_sensor_data)  # 2Hz
        self.x = 0.0
        self.y = 0.0
        self.theta = 0.0
        self.get_logger().info('Sensor Publisher initialized.')

    def publish_sensor_data(self):
        msg = Pose()
        # Simulasi pergerakan acak
        self.x += random.uniform(-0.5, 0.5)
        self.y += random.uniform(-0.5, 0.5)
        self.theta += random.uniform(-0.1, 0.1)

        msg.position.x = self.x
        msg.position.y = self.y
        msg.position.z = 0.0
        msg.orientation.z = math.sin(self.theta / 2.0)
        msg.orientation.w = math.cos(self.theta / 2.0)

        self.publisher_.publish(msg)
        self.get_logger().info(f'Published sensor data: x={self.x:.2f}, y={self.y:.2f}, θ={self.theta:.2f}')

def main(args=None):
    rclpy.init(args=args)
    node = SensorPublisher()
    rclpy.spin(node)
    node.destroy_node()
    rclpy.shutdown()

if __name__ == '__main__':
    main()
