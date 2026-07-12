import rclpy
from rclpy.node import Node
from sensor_msgs.msg import JointState
from visualization_msgs.msg import Marker

from arm_ik.ik import ik

JOINTS = ["joint1", "joint2", "joint3", "finger_left", "finger_right"]
OPEN = 0.012
RATE = 30.0
HOLD = 3.0      # pause at home
TRAVEL = 5.0    # home -> target
STAY = 3.0      # pause on the target (fingers grab here)
BACK = 3.0      # target -> home
CYCLE = HOLD + TRAVEL + STAY + BACK


def smoothstep(a, b, t):
    t = max(0.0, min(1.0, t))
    return a + (b - a) * t * t * (3 - 2 * t)


class MoveArm(Node):
    def __init__(self):
        super().__init__("move_arm")
        self.declare_parameter("target_x", 0.30)
        self.declare_parameter("target_y", 0.15)
        self.declare_parameter("target_z", 0.25)
        x = self.get_parameter("target_x").value
        y = self.get_parameter("target_y").value
        z = self.get_parameter("target_z").value

        self.goal = ik(x, y, z)
        if self.goal is None:
            self.get_logger().error("target (%.2f, %.2f, %.2f) is out of reach - staying home" % (x, y, z))
            self.goal = (0.0, 0.0, 0.0)
        else:
            self.get_logger().info("target (%.2f, %.2f, %.2f) -> joints (%.2f, %.2f, %.2f)"
                                   % (x, y, z, *self.goal))

        self.marker = Marker()
        self.marker.header.frame_id = "base_link"
        self.marker.type = Marker.SPHERE
        self.marker.pose.position.x = x
        self.marker.pose.position.y = y
        self.marker.pose.position.z = z
        self.marker.pose.orientation.w = 1.0
        self.marker.scale.x = self.marker.scale.y = self.marker.scale.z = 0.035
        self.marker.color.r = 1.0
        self.marker.color.a = 1.0

        self.js_pub = self.create_publisher(JointState, "/joint_states", 10)
        self.marker_pub = self.create_publisher(Marker, "/target_marker", 10)
        self.grip = 0.0
        self.start = self.get_clock().now()
        self.create_timer(1.0 / RATE, self.tick)

    def tick(self):
        t = ((self.get_clock().now() - self.start).nanoseconds / 1e9) % CYCLE
        if t < HOLD:
            frac = 0.0
        elif t < HOLD + TRAVEL:
            frac = (t - HOLD) / TRAVEL
        elif t < HOLD + TRAVEL + STAY:
            frac = 1.0
        else:
            frac = (CYCLE - t) / BACK

        # fingers close while sitting on the target
        grab = HOLD + TRAVEL + 0.3 < t < HOLD + TRAVEL + STAY - 0.6
        step = 1.0 / RATE / 0.6
        self.grip = min(self.grip + step, 1.0) if grab else max(self.grip - step, 0.0)

        js = JointState()
        js.header.stamp = self.get_clock().now().to_msg()
        js.name = JOINTS
        js.position = [smoothstep(0.0, g, frac) for g in self.goal] + [OPEN * (1 - self.grip)] * 2
        self.js_pub.publish(js)
        self.marker_pub.publish(self.marker)


def main():
    rclpy.init()
    node = MoveArm()
    try:
        rclpy.spin(node)
    except KeyboardInterrupt:
        pass
    rclpy.shutdown()


if __name__ == "__main__":
    main()
