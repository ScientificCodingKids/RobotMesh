#Qualifier #2 code
#super_urgent_remote

import vex

#region config
brain       = vex.Brain()
driveright  = vex.Motor(vex.Ports.PORT1, vex.GearSetting.RATIO18_1, False)
armright    = vex.Motor(vex.Ports.PORT4, vex.GearSetting.RATIO18_1, False)
armleft     = vex.Motor(vex.Ports.PORT8, vex.GearSetting.RATIO18_1, True)
driveleft   = vex.Motor(vex.Ports.PORT10, vex.GearSetting.RATIO18_1, True)
claw        = vex.Motor(vex.Ports.PORT13, vex.GearSetting.RATIO18_1, False)
dt          = vex.Drivetrain(driveleft, driveright, 319.1764, 292.1, vex.DistanceUnits.MM)
controller1 = vex.Controller(vex.ControllerType.PRIMARY)
#endregion config

competition = vex.Competition()

def driver():
  armleft.set_velocity(20, vex.VelocityUnits.PCT)
  armleft.set_max_torque_percent(100, vex.PercentUnits.PCT)
  armright.set_velocity(20, vex.VelocityUnits.PCT)
  armright.set_max_torque_percent(100, vex.PercentUnits.PCT)
  while True:
    if controller1.buttonL1.pressing():
      claw.spin(vex.DirectionType.FWD)
    elif controller1.buttonL2.pressing():
      claw.spin(vex.DirectionType.REV)
    else:
      claw.set_stopping(vex.BrakeType.HOLD)
      claw.stop(vex.BrakeType.HOLD)
    if controller1.buttonR1.pressing():
      armright.spin(vex.DirectionType.FWD)
    elif controller1.buttonR2.pressing():
      armright.spin(vex.DirectionType.REV)
    else:
      armright.set_stopping(vex.BrakeType.HOLD)
      armright.stop(vex.BrakeType.HOLD)
    if controller1.buttonR1.pressing():
      armleft.spin(vex.DirectionType.FWD)
    elif controller1.buttonR2.pressing():
      armleft.spin(vex.DirectionType.REV)
    else:
      armleft.set_stopping(vex.BrakeType.HOLD)
      armleft.stop(vex.BrakeType.HOLD)
    driveleft.set_velocity(50, vex.VelocityUnits.PCT)
    if controller1.axis3.position(vex.PercentUnits.PCT) > 15:
      driveleft.spin(vex.DirectionType.FWD)
    elif controller1.axis3.position(vex.PercentUnits.PCT) < -15:
      driveleft.spin(vex.DirectionType.REV)
    else:
      driveleft.stop(vex.BrakeType.HOLD)
    driveright.set_velocity(50, vex.VelocityUnits.PCT)
    if controller1.axis2.position(vex.PercentUnits.PCT) > 15:
      driveright.spin(vex.DirectionType.FWD)
    elif controller1.axis2.position(vex.PercentUnits.PCT) < -15:
      driveright.spin(vex.DirectionType.REV)
    else:
      driveright.stop(vex.BrakeType.HOLD)
competition.drivercontrol(driver)

def auto():
  dt.set_velocity(100, vex.VelocityUnits.PCT)
  dt.drive_for(vex.DirectionType.REV, 15, vex.DistanceUnits.IN)
  dt.drive_for(vex.DirectionType.FWD, 8, vex.DistanceUnits.IN)
competition.autonomous(auto)

