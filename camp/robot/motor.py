import grove_i2c_motor_driver as grove


class MotorDriver(object):
    def __init__(self):
        self.driver = grove.motor_driver()
        self.left = 0
        self.right = 0
        self.left_forward = True
        self.right_forward = True

    def setRightSpeed(self, speed):
        if speed < 0:
            speed = 0 - speed
            self.right_forward = False
            self.driver.MotorSpeedSetAB(speed, self.left)
        else:
            self.right_forward = True
            self.driver.MotorSpeedSetAB(speed, self.left)

        self.right = speed
        direction = 0
        if self.left_forward:
            direction |= 1 << 3
        else:
            direction |= 1 << 2
        if self.right_forward:
            direction |= 1 << 1
        else:
            direction |= 1
        self.driver.MotorDirectionSet(direction)

    def setLeftSpeed(self, speed):
        if speed < 0:
            speed = 0 - speed
            self.left_forward = False
            self.driver.MotorSpeedSetAB(self.right, speed)
        else:
            self.left_forward = True
            self.driver.MotorSpeedSetAB(self.right, speed)

        self.left = speed
        direction = 0
        if self.left_forward:
            direction |= 1 << 3
        else:
            direction |= 1 << 2
        if self.right_forward:
            direction |= 1 << 1
        else:
            direction |= 1
        self.driver.MotorDirectionSet(direction)

    def stop(self):
        self.setLeftSpeed(0)
        self.setRightSpeed(0)
