# Robot Simulation

Simulation in WPILib allows for code and logic to be tested onboard your computer, rather than physical hardware. It's exceptionally useful for when construction has not built the robot, but you have code to run!

There are a few different facets of simulation to take note of before you can start, including:

- [The Simulation GUI](https://docs.wpilib.org/en/stable/docs/software/wpilib-tools/robot-simulation)
- [WPILIB's simulation classes](#simulation-classes)
  - [Physics simulators](https://docs.wpilib.org/en/stable/docs/software/wpilib-tools/robot-simulation/physics-sim.html)
  - [Mechanism2d](https://docs.wpilib.org/en/stable/docs/software/dashboards/glass/mech2d-widget.html)
  - [Field2d](https://docs.wpilib.org/en/stable/docs/software/dashboards/glass/field2d-widget.html)
- [Logging & Dashboards](#logging--dashboards)

## Logging & Dashboards

In testing, it is common to want to directly observe robot measurements and values in order to tune your systems or debug. This is also incredibly important when working with simulation, as you otherwise have no reference to what is going on without a physical robot.

For more details, visit [our doc](/Telemetry.md).

## Simulation Classes

This section will heavily reference the WPILIB docs [here](https://docs.wpilib.org/en/stable/docs/software/wpilib-tools/robot-simulation/introduction.html).

Before doing anything with simulation, make sure desktop support is turned on. Follow [these instructions](https://docs.wpilib.org/en/stable/docs/software/wpilib-tools/robot-simulation/introduction.html). Use [the next doc](https://docs.wpilib.org/en/stable/docs/software/wpilib-tools/robot-simulation) as reference for the GUI when working with it (same as above).

WPILIB contains generic simulation classes for different mechanisms (like `ElevatorSim`) based on physical details and constraints about your system. You can see a full list of them and examples on using them [here](https://docs.wpilib.org/en/stable/docs/software/wpilib-tools/robot-simulation/physics-sim.html).

There's also the specific widget classes `Field2d` and `Mechanism2d`, which allow for pixel representations of the field and parts of mechanisms.

Physical objects, like game pieces, wheels, the drivetrain, etc., can be added to the Field2d object, allowing for nice representations without a real field. [Here's more](https://docs.wpilib.org/en/stable/docs/software/dashboards/glass/field2d-widget.html) on how you can use it.

Mechanism2ds allow for block representations of mechanisms. This is most commonly used for simulating arms and elevators. See [the docs](https://docs.wpilib.org/en/stable/docs/software/dashboards/glass/mech2d-widget.html) for usage details and further clarifications.
