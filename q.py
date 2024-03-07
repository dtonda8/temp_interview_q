"""
Documentation allowed: 
- geometry_msgs/Twist: http://docs.ros.org/en/noetic/api/geometry_msgs/html/msg/Twist.html
- _twist.py file: http://docs.ros.org/en/diamondback/api/geometry_msgs/html/__Twist_8py_source.html
- _Vector3.py file: http://docs.ros.org/en/diamondback/api/geometry_msgs/html/__Vector3_8py_source.html#l00006
- ROS 2 API docs: https://docs.ros2.org/foxy/api/rclpy/api/topics.html#module-rclpy.publisher
"""
# Ignore import errors, if any
import rclpy
from geometry_msgs.msg import Twist

def main():
    rclpy.init()
    node = rclpy.create_node('twist_controller_node')
    pub = node.create_publisher(geometry_msgs.msg.Twist, 'twist_cmd', 10)
    
    linear_x = 3.5
    angular_z = 1

    msg = Twist()
    # TODO: Understand the Twist message format and update the msg variable to 
    # to have it's linear x attribute set to  linear_x and its angular z 
    # attribute set to angular_z
    
    # TODO: Publish the Twist message to the 'twist_cmd' topic publish() method
    
    # End of problem

if __name__ == '__main__':
    main()