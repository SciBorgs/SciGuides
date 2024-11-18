# [Fundamentals of Sensors](https://docs.wpilib.org/en/stable/docs/software/hardware-apis/sensors/sensor-overview-software.html#sensor-overview-software)

This aims to be an brief reference to the different sensors that you will most commonly see and use on the robot. For further details, see the linked materials or consult your favorite search engine.

## [Encoders](https://docs.wpilib.org/en/stable/docs/software/hardware-apis/sensors/encoders-software.html#encoders-software)

They measure rotation. Many brushless motors have encoders integrated inside of them, while others can be found outside of the robot. Most measure what is effectively rotational displacement, as encoders read negative values from relative backwards movement.

All encoders have some sort of default unit. Various vendors will have different methods of changing the units returned; read their docs!

### [Relative Encoders](https://docs.wpilib.org/en/stable/docs/software/hardware-apis/sensors/sensor-overview-software.html#sensor-overview-software)

When powered on, its distance measurement will read 0. The zero-point will change on code boot, making its measurements "relative" to whenever it started.

### [Absolute Encoders](https://docs.wpilib.org/en/stable/docs/software/hardware-apis/sensors/encoders-software.html#encoders-software)

Has a set zero point. Will always know where it is, even between code deploys.

## [Gyroscope](https://docs.wpilib.org/en/stable/docs/software/hardware-apis/sensors/gyros-software.html)

It measures the rate of rotation of whatever plane it is on (and sometimes its relative axes). Usually found on the base of the drivetrain.

## [Beambreaks]()

Detect if something has passed through them. Two key components: a part that shoots a ray of light, and a receiver. When the receiver no longer detects light, a signal is returned.

For our program, beambreak sensors return true when unblocked, and false when blocked. **THIS IS SUBJECT TO CHANGE.**

## [Cameras](https://docs.photonvision.org/en/latest/docs/integration/aprilTagStrategies.html)

Using the known position of a camera and the known position of targets in its view, the target-relative and field-relative position of a robot can be calculated. These can be used to auto-correct odometry, auto-aim towards a target, or [automate movement entirely](https://www.youtube.com/watch?v=2zB0w69P4mc&t=73s).

## [Interactions with Software](https://docs.wpilib.org/en/stable/docs/software/hardware-apis/sensors/digital-inputs-software.html#digital-inputs-software)

From a code perspective, nearly all will be integrated into hardware (that can be interacted with their apis) or plugged into the RoboRIO (that can be interacted with using built-in WPILib classes, like `RelativeEncoder` or `DigitalInput`).