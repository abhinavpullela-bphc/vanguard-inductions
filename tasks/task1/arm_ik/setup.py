from setuptools import setup

package_name = "arm_ik"

setup(
    name=package_name,
    version="0.0.1",
    packages=[package_name],
    data_files=[
        ("share/ament_index/resource_index/packages", ["resource/" + package_name]),
        ("share/" + package_name, ["package.xml"]),
        ("share/" + package_name + "/urdf", ["urdf/arm3dof.urdf"]),
        ("share/" + package_name + "/launch", ["launch/display.launch.py", "launch/demo.launch.py"]),
        ("share/" + package_name + "/rviz", ["rviz/arm.rviz"]),
    ],
    install_requires=["setuptools"],
    zip_safe=True,
    maintainer="Abhinav Pullela",
    maintainer_email="f20251199@hyderabad.bits-pilani.ac.in",
    description="3DOF arm with analytic inverse kinematics",
    license="MIT",
    entry_points={
        "console_scripts": [
            "move_arm = arm_ik.move_arm:main",
        ],
    },
)
