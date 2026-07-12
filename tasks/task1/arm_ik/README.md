# arm_ik

A 3DOF arm with a hand-written analytic inverse kinematics solver. The URDF builds the arm,
`ik.py` works out the joint angles for a target point, and `move_arm.py` drives the arm from
its home pose to that point in RViz2, grabs it, and returns.

Build (inside the container's `~/vanguard_ws`):

    colcon build --packages-select arm_ik
    source install/setup.bash

Run the demo (RViz opens and the arm cycles: home, move to the red ball, grab, return):

    ros2 launch arm_ik demo.launch.py

The target is not fixed - it can be any reachable point, default (0.30, 0.15, 0.25):

    ros2 launch arm_ik demo.launch.py target_x:=0.15 target_y:=-0.30 target_z:=0.40

Unreachable points are rejected with an error and the arm stays home.

To just look at the arm and jog the joints by hand:

    ros2 launch arm_ik display.launch.py gui:=true

`python3 arm_ik/ik.py` runs a self-check: 20 random reachable points, confirming fk(ik(p))=p.

If RViz shows a black screen in the noVNC desktop, run `export LIBGL_ALWAYS_SOFTWARE=1`
before launching.
