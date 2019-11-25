import vex
import sys

#region config
brain = vex.Brain()
driveright = vex.Motor(vex.Ports.PORT1, vex.GearSetting.RATIO18_1, False)
armright = vex.Motor(vex.Ports.PORT4, vex.GearSetting.RATIO18_1, False)
armleft = vex.Motor(vex.Ports.PORT8, vex.GearSetting.RATIO18_1, True)
driveleft = vex.Motor(vex.Ports.PORT10, vex.GearSetting.RATIO18_1, False)
claw = vex.Motor(vex.Ports.PORT13, vex.GearSetting.RATIO18_1, False)
dt = vex.Drivetrain(driveleft, driveright, 319.1764, 292.1, vex.DistanceUnits.MM)
controller1 = vex.Controller(vex.ControllerType.PRIMARY)
#endregion config

def thread2():
    while True:
        if controller1.buttonR1.pressing():
            armleft.spin(vex.DirectionType.FWD)
        else:
            armleft.stop(vex.BrakeType.BRAKE)
    sys.run_in_thread(thread2)


# main thread
armright.set_stopping(vex.BrakeType.HOLD)
armleft.set_stopping(vex.BrakeType.HOLD)
armright.set_velocity(40, vex.VelocityUnits.PCT)
armleft.set_velocity(40, vex.VelocityUnits.PCT)

while True:
    if controller1.buttonR1.pressing():
        armright.spin(vex.DirectionType.FWD)
    else:
        armright.stop(vex.BrakeType.BRAKE)

None if controller1.buttonR1.pressing() else None

if False:
    pass

armleft.spin(vex.DirectionType.FWD)

armright.spin(vex.DirectionType.FWD)