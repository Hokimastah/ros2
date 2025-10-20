import rclpy
from rclpy.node import Node
from geometry_msgs.msg import Pose
import math
import time

class DataProcessor(Node):
    def __init__(self):
        super().__init__('data_processor')
        self.subscription = self.create_subscription(
            Pose, 'sensor_data', self.listener_callback, 10)
        self.prev_x = None
        self.prev_y = None
        self.prev_time = time.time()
        self.get_logger().info('Data Processor initialized.')

    def listener_callback(self, msg):
        current_time = time.time()
        if self.prev_x is not None:
            dt = current_time - self.prev_time
            distance = math.sqrt((msg.position.x - self.prev_x) ** 2 + (msg.position.y - self.prev_y) ** 2)
            velocity = distance / dt if dt > 0 else 0.0

            self.get_logger().info(f'Real-time velocity: {velocity:.2f} m/s')
        
        # Simpan data terakhir
        self.prev_x = msg.position.x
        self.prev_y = msg.position.y
        self.prev_time = current_time

def main(args=None):
    rclpy.init(args=args)
    node = DataProcessor()
    rclpy.spin(node)
    node.destroy_node()
    rclpy.shutdown()

if __name__ == '__main__':
    main()
