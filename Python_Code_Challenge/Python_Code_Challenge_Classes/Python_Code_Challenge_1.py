# Define the DriveBot class here!

# print(robot_1.motor_speed)
# print(robot_1.direction)
# print(robot_1.sensor_range)
class DriveBot:
    def __init__(self):
        self.motor_speed = 0
        self.direction = 0
        self.sensor_range = 0

robot_1 = DriveBot()
robot_1.motor_speed = 5
robot_1.direction = 90
robot_1.sensor_range = 10