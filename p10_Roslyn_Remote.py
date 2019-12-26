"""__CONFIG__
{"version":20,"widgetInfos":[{"hwid":"1","name":"Right_Drive","typeName":"motor","extraConfig":{"gearSetting":1,"reverse":true},"bufferIndex":0},{"hwid":"4","name":"rightup","typeName":"motor","extraConfig":{"gearSetting":1,"reverse":false},"bufferIndex":1},{"hwid":"5","name":"leftdown","typeName":"motor","extraConfig":{"gearSetting":1,"reverse":false},"bufferIndex":2},{"hwid":"6","name":"leftup","typeName":"motor","extraConfig":{"gearSetting":1,"reverse":true},"bufferIndex":3},{"hwid":"7","name":"rightdown","typeName":"motor","extraConfig":{"gearSetting":1,"reverse":true},"bufferIndex":4},{"hwid":"10","name":"Left_Drive","typeName":"motor","extraConfig":{"gearSetting":1,"reverse":false},"bufferIndex":5},{"hwid":"20","name":"Claw","typeName":"motor","extraConfig":{"gearSetting":1,"reverse":false},"bufferIndex":6},{"hwid":"triport_adi","name":"triport_22","typeName":"triport","extraConfig":null,"bufferIndex":7},{"hwid":"drivetrain","name":"dt","typeName":"drivetrain","extraConfig":{"leftMotorHwId":"10","rightMotorHwId":"1","wheelTravel":319.1764,"trackWidth":292.1},"bufferIndex":8},{"hwid":"controller","name":"con","typeName":"controller_one","extraConfig":null,"bufferIndex":9},{"hwid":"Axis1","name":"axis1","typeName":"controller_axis","extraConfig":null,"bufferIndex":10},{"hwid":"Axis2","name":"axis2","typeName":"controller_axis","extraConfig":null,"bufferIndex":11},{"hwid":"Axis3","name":"axis3","typeName":"controller_axis","extraConfig":null,"bufferIndex":12},{"hwid":"Axis4","name":"axis4","typeName":"controller_axis","extraConfig":null,"bufferIndex":13},{"hwid":"ButtonL1","name":"buttonL1","typeName":"controller_button","extraConfig":null,"bufferIndex":14},{"hwid":"ButtonL2","name":"buttonL2","typeName":"controller_button","extraConfig":null,"bufferIndex":15},{"hwid":"ButtonR1","name":"buttonR1","typeName":"controller_button","extraConfig":null,"bufferIndex":16},{"hwid":"ButtonR2","name":"buttonR2","typeName":"controller_button","extraConfig":null,"bufferIndex":17},{"hwid":"ButtonUp","name":"buttonUp","typeName":"controller_button","extraConfig":null,"bufferIndex":18},{"hwid":"ButtonDown","name":"buttonDown","typeName":"controller_button","extraConfig":null,"bufferIndex":19},{"hwid":"ButtonLeft","name":"buttonLeft","typeName":"controller_button","extraConfig":null,"bufferIndex":20},{"hwid":"ButtonRight","name":"buttonRight","typeName":"controller_button","extraConfig":null,"bufferIndex":21},{"hwid":"ButtonX","name":"buttonX","typeName":"controller_button","extraConfig":null,"bufferIndex":22},{"hwid":"ButtonB","name":"buttonB","typeName":"controller_button","extraConfig":null,"bufferIndex":23},{"hwid":"ButtonY","name":"buttonY","typeName":"controller_button","extraConfig":null,"bufferIndex":24},{"hwid":"ButtonA","name":"buttonA","typeName":"controller_button","extraConfig":null,"bufferIndex":25}]}"""
"""__BLOCKLY__
<xml xmlns="http://www.w3.org/1999/xhtml"><block type="vexv5_start_autonomous" id="+`-8#WHI-uN6akLo6?VE" x="-94" y="64"><next><block type="vexv5_drivetrain_set_velocity" id="j+%WeLUyxpCr?7]mbTc2"><field name="p1">PCT</field><value name="p0"><block type="math_number" id="Q|qr=A(xU:fcoej9KORE"><field name="NUM">100</field></block></value><next><block type="vexv5_drivetrain_drive_for" id="Y%VR5=]nq=f^JRO9S{TN"><field name="p0">REV</field><field name="p2">CM</field><value name="p1"><block type="math_number" id="(K=;aoAl[LdG:x7gwaO0"><field name="NUM">50</field></block></value><next><block type="vexv5_drivetrain_drive_for" id="oYM/UzGUMBhXr[yfa1Y0"><field name="p0">FWD</field><field name="p2">CM</field><value name="p1"><block type="math_number" id="jUYf:{e6*xnq0Ektym#;"><field name="NUM">15</field></block></value></block></next></block></next></block></next></block><block type="vexv5_start_drivercontrol" id="5;~Y~/yCZ5xOIoHpAS=|" x="250" y="50"><next><block type="controls_forever" id="vXrx=98HQ[+m]Jf}Ep_@"><statement name="DO"><block type="controls_if" id="aI;2:msCrA2tuS/E,M@t"><mutation elseif="1" else="1"></mutation><value name="IF0"><block type="vexv5_controller_button_pressing" id="ZoD.f{21O]MPRYt3VDH5"><field name="WIDGET_ID">ButtonR1</field></block></value><statement name="DO0"><block type="spin_without_velocity" id="BlfcHiel#GMMTIicgO4."><field name="WIDGET_ID">4</field><field name="p0">FWD</field></block></statement><value name="IF1"><block type="vexv5_controller_button_pressing" id="um*~JQSkAC.8OiNShd|A"><field name="WIDGET_ID">ButtonR2</field></block></value><statement name="DO1"><block type="spin_without_velocity" id="@.O3tAo^6#/f25(.}Y0U"><field name="WIDGET_ID">4</field><field name="p0">REV</field></block></statement><statement name="ELSE"><block type="vexv5_motor_stop" id="c]!Sk;B9X;gdbHWLBB)N"><field name="WIDGET_ID">4</field><field name="p0">HOLD</field></block></statement><next><block type="controls_if" id="rY~u=ui_8@;a3]4]et,c"><mutation elseif="1" else="1"></mutation><value name="IF0"><block type="vexv5_controller_button_pressing" id="*#BHM}uXPRovJ`-ANBc^"><field name="WIDGET_ID">ButtonR1</field></block></value><statement name="DO0"><block type="spin_without_velocity" id="^.0|9i1aer3syqFa]~x~"><field name="WIDGET_ID">5</field><field name="p0">FWD</field></block></statement><value name="IF1"><block type="vexv5_controller_button_pressing" id="EOmA5PYNG9},K9b!{]{,"><field name="WIDGET_ID">ButtonR2</field></block></value><statement name="DO1"><block type="spin_without_velocity" id="dx^#(lm8Tj:NxFww^qiY"><field name="WIDGET_ID">5</field><field name="p0">REV</field></block></statement><statement name="ELSE"><block type="vexv5_motor_stop" id="rsj?-2BSAQzZ_/a(HM`Y"><field name="WIDGET_ID">5</field><field name="p0">HOLD</field></block></statement><next><block type="controls_if" id="BtCNezY#[04Nf1(|sa*a"><mutation elseif="1" else="1"></mutation><value name="IF0"><block type="vexv5_controller_button_pressing" id="A}W]kCcc{3;iW9/BM)J,"><field name="WIDGET_ID">ButtonR1</field></block></value><statement name="DO0"><block type="spin_without_velocity" id="2=YU[s8q)#T+Vn}]_RL="><field name="WIDGET_ID">6</field><field name="p0">FWD</field></block></statement><value name="IF1"><block type="vexv5_controller_button_pressing" id="ZwR~:K:A+yJCuDpMvQ4t"><field name="WIDGET_ID">ButtonR2</field></block></value><statement name="DO1"><block type="spin_without_velocity" id="eA7%K4%[I99Y@V=bbIe9"><field name="WIDGET_ID">6</field><field name="p0">REV</field></block></statement><statement name="ELSE"><block type="vexv5_motor_stop" id="=.)@h)#qx4dxCgkgOPW]"><field name="WIDGET_ID">6</field><field name="p0">HOLD</field></block></statement><next><block type="controls_if" id="?@(fVKzGP?+!OVmy6wk~"><mutation elseif="1" else="1"></mutation><value name="IF0"><block type="vexv5_controller_button_pressing" id="~vMvaw31.5~eg]3[UOAd"><field name="WIDGET_ID">ButtonR1</field></block></value><statement name="DO0"><block type="spin_without_velocity" id="z*aU}}c/gSCYhofgyzut"><field name="WIDGET_ID">7</field><field name="p0">FWD</field></block></statement><value name="IF1"><block type="vexv5_controller_button_pressing" id="*dZXvOZo/y/+|MC-rHh1"><field name="WIDGET_ID">ButtonR2</field></block></value><statement name="DO1"><block type="spin_without_velocity" id="YNdNybwI@,eO~}YL_q)g"><field name="WIDGET_ID">7</field><field name="p0">REV</field></block></statement><statement name="ELSE"><block type="vexv5_motor_stop" id=")Kf8b`hF6Q/S/Lvhpc5g"><field name="WIDGET_ID">7</field><field name="p0">HOLD</field></block></statement><next><block type="variables_set" id="ASMq36V2IJij1Lt9oejx"><field name="VAR">LeftMotorSpeed</field><value name="VALUE"><block type="math_arithmetic" id="_pcWM9d!v]NpJ9YWzIIe"><field name="OP">MULTIPLY</field><value name="A"><block type="vexv5_controller_axis_position" id="yXK40,oh,?wE#r_6}*_`"><field name="WIDGET_ID">Axis3</field></block></value><value name="B"><block type="math_number" id=":;FBhxfnGJ6ThQT*fQH{"><field name="NUM">0.5</field></block></value></block></value><next><block type="controls_if" id="ZrF@,:Hj-z6SeH=t;[}I"><mutation else="1"></mutation><value name="IF0"><block type="logic_compare" id=":,)%Vdu-Eng^GZ{zxS}o"><field name="OP">GT</field><value name="A"><block type="math_single" id="1Q?jrlZ`6uLX%8?4;W7Z"><field name="OP">ABS</field><value name="NUM"><block type="variables_get" id="Mg_`T7.K*:]EO]_!1Bbp"><field name="VAR">LeftMotorSpeed</field></block></value></block></value><value name="B"><block type="math_number" id="Q1ho*jfSz[tXjHxUSYms"><field name="NUM">5</field></block></value></block></value><statement name="DO0"><block type="vexv5_motor_set_velocity" id="7r%+nbcNRLzNva8itL;^"><field name="WIDGET_ID">10</field><field name="p1">PCT</field><value name="p0"><block type="variables_get" id="Df8inE:1o9IHI^}xA[vl"><field name="VAR">LeftMotorSpeed</field></block></value><next><block type="spin_without_velocity" id="Xjly8Ndv`UG}}Lq-#p2L"><field name="WIDGET_ID">10</field><field name="p0">FWD</field></block></next></block></statement><statement name="ELSE"><block type="vexv5_motor_stop" id="fc4RoZWk@/#rt|pe/abp"><field name="WIDGET_ID">10</field><field name="p0">HOLD</field></block></statement><next><block type="variables_set" id="{m7MF@jRi9qQ4td[P+p*"><field name="VAR">RightMotorSpeed</field><value name="VALUE"><block type="math_arithmetic" id="wM=P_aZulm6l%)Y9T0;N"><field name="OP">MULTIPLY</field><value name="A"><block type="vexv5_controller_axis_position" id="RJ3:jYM~8Wh^2`v9#XhG"><field name="WIDGET_ID">Axis2</field></block></value><value name="B"><block type="math_number" id="|pA)AyW.LV^iM!LRm)C2"><field name="NUM">0.5</field></block></value></block></value><next><block type="controls_if" id="(sKNDt0O9Lb#V}Cp+vVK"><mutation else="1"></mutation><value name="IF0"><block type="logic_compare" id="gsl5DN(OOAI#ISvV%QAW"><field name="OP">GT</field><value name="A"><block type="math_single" id="YM-.x#{Q!|:u=YSv81p;"><field name="OP">ABS</field><value name="NUM"><block type="variables_get" id="HnOuUIAFr(.+)5w5kF[`"><field name="VAR">RightMotorSpeed</field></block></value></block></value><value name="B"><block type="math_number" id="hT]=AX/Q,HhYTq~KwmqQ"><field name="NUM">5</field></block></value></block></value><statement name="DO0"><block type="vexv5_motor_set_velocity" id="V`#o64|Dxg*DwBedEk^="><field name="WIDGET_ID">1</field><field name="p1">PCT</field><value name="p0"><block type="variables_get" id="B|e4zU/[~4T`*S?T]nKp"><field name="VAR">RightMotorSpeed</field></block></value><next><block type="spin_without_velocity" id="xqIC_aMRvlB/)Jg#.-FL"><field name="WIDGET_ID">1</field><field name="p0">FWD</field></block></next></block></statement><statement name="ELSE"><block type="vexv5_motor_stop" id="wkg0K[I5P4BjlwYBStU}"><field name="WIDGET_ID">1</field><field name="p0">HOLD</field></block></statement><next><block type="controls_if" id=":OJQ6D~_EP*E]KR%e[p6"><mutation elseif="1" else="1"></mutation><value name="IF0"><block type="vexv5_controller_button_pressing" id="{06)ed(w}8C){%MW_/[,"><field name="WIDGET_ID">ButtonL1</field></block></value><statement name="DO0"><block type="spin_without_velocity" id="D[Lt?t!Q_.Lqh5yOBvL%"><field name="WIDGET_ID">20</field><field name="p0">FWD</field></block></statement><value name="IF1"><block type="vexv5_controller_button_pressing" id="XnQ0g4S([ETFz@^IPgtI"><field name="WIDGET_ID">ButtonL2</field></block></value><statement name="DO1"><block type="spin_without_velocity" id="uF;MQ0.2p/,MS)g8hLn3"><field name="WIDGET_ID">20</field><field name="p0">REV</field></block></statement><statement name="ELSE"><block type="vexv5_motor_stop" id="*Y%LKCRpyWfhzJ|LM2_H"><field name="WIDGET_ID">20</field><field name="p0">HOLD</field></block></statement></block></next></block></next></block></next></block></next></block></next></block></next></block></next></block></next></block></statement></block></next></block></xml>
"""

import vex
import math

#region config
brain       = vex.Brain()
Right_Drive = vex.Motor(vex.Ports.PORT1, vex.GearSetting.RATIO18_1, True)
rightup     = vex.Motor(vex.Ports.PORT4, vex.GearSetting.RATIO18_1, False)
leftdown    = vex.Motor(vex.Ports.PORT5, vex.GearSetting.RATIO18_1, False)
leftup      = vex.Motor(vex.Ports.PORT6, vex.GearSetting.RATIO18_1, True)
rightdown   = vex.Motor(vex.Ports.PORT7, vex.GearSetting.RATIO18_1, True)
Left_Drive  = vex.Motor(vex.Ports.PORT10, vex.GearSetting.RATIO18_1, False)
Claw        = vex.Motor(vex.Ports.PORT20, vex.GearSetting.RATIO18_1, False)
dt          = vex.Drivetrain(Left_Drive, Right_Drive, 319.1764, 292.1, vex.DistanceUnits.MM)
con         = vex.Controller(vex.ControllerType.PRIMARY)
#endregion config

LeftMotorSpeed = None
RightMotorSpeed = None

competition = vex.Competition()

def auto():
  dt.set_velocity(100, vex.VelocityUnits.PCT)
  dt.drive_for(vex.DirectionType.REV, 50, vex.DistanceUnits.CM)
  dt.drive_for(vex.DirectionType.FWD, 15, vex.DistanceUnits.CM)
competition.autonomous(auto)

def driver():
  global LeftMotorSpeed, RightMotorSpeed
  while True:
    if con.buttonR1.pressing():
      rightup.spin(vex.DirectionType.FWD)
    elif con.buttonR2.pressing():
      rightup.spin(vex.DirectionType.REV)
    else:
      rightup.stop(vex.BrakeType.HOLD)
    if con.buttonR1.pressing():
      leftdown.spin(vex.DirectionType.FWD)
    elif con.buttonR2.pressing():
      leftdown.spin(vex.DirectionType.REV)
    else:
      leftdown.stop(vex.BrakeType.HOLD)
    if con.buttonR1.pressing():
      leftup.spin(vex.DirectionType.FWD)
    elif con.buttonR2.pressing():
      leftup.spin(vex.DirectionType.REV)
    else:
      leftup.stop(vex.BrakeType.HOLD)
    if con.buttonR1.pressing():
      rightdown.spin(vex.DirectionType.FWD)
    elif con.buttonR2.pressing():
      rightdown.spin(vex.DirectionType.REV)
    else:
      rightdown.stop(vex.BrakeType.HOLD)
    LeftMotorSpeed = con.axis3.position(vex.PercentUnits.PCT) * 0.5
    if math.fabs(LeftMotorSpeed) > 5:
      Left_Drive.set_velocity(LeftMotorSpeed, vex.VelocityUnits.PCT)
      Left_Drive.spin(vex.DirectionType.FWD)
    else:
      Left_Drive.stop(vex.BrakeType.HOLD)
    RightMotorSpeed = con.axis2.position(vex.PercentUnits.PCT) * 0.5
    if math.fabs(RightMotorSpeed) > 5:
      Right_Drive.set_velocity(RightMotorSpeed, vex.VelocityUnits.PCT)
      Right_Drive.spin(vex.DirectionType.FWD)
    else:
      Right_Drive.stop(vex.BrakeType.HOLD)
    if con.buttonL1.pressing():
      Claw.spin(vex.DirectionType.FWD)
    elif con.buttonL2.pressing():
      Claw.spin(vex.DirectionType.REV)
    else:
      Claw.stop(vex.BrakeType.HOLD)
competition.drivercontrol(driver)

