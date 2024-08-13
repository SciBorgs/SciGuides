# Robot Simulation

Simulation in WPILib allows for code and logic to be tested onboard your computer, rather than physical hardware. It's exceptionally useful for when construction has not built the robot, but you have code to run!

There are a few different facets of simulation to take note of before you can start, including:

- [The Simulation GUI](https://docs.wpilib.org/en/stable/docs/software/wpilib-tools/robot-simulation)
- [WPILIB's simulation classes](#simulation-classes)
  - [Physics simulators](https://docs.wpilib.org/en/stable/docs/software/wpilib-tools/robot-simulation/physics-sim.html)
  - [Mechanism2d](https://docs.wpilib.org/en/stable/docs/software/dashboards/glass/mech2d-widget.html)
  - [Field2d](https://docs.wpilib.org/en/stable/docs/software/dashboards/glass/field2d-widget.html)
- Logging & Dashboards

## Logging & Log Viewers

In testing, it is common to want to directly observe robot measurements and values in order to tune your systems or debug. This is also incredibly important when working with simulation, as you otherwise have no reference to what is going on without a physical robot. For more details, visit [the docs](https://docs.wpilib.org/en/stable/docs/software/telemetry/telemetry.html).

On the SciBorgs, we currently use [Monologue](https://github.com/shueja/Monologue/wiki) (general) and [URCL](https://github.com/Mechanical-Advantage/URCL) (for REV motors), both third-party logging programs. More options can be found [here](https://docs.wpilib.org/en/stable/docs/software/telemetry/3rd-party-libraries.html).

On the data-viewing end, we like 

## Simulation Classes

This section will heavily reference the WPILIB docs [here](https://docs.wpilib.org/en/stable/docs/software/wpilib-tools/robot-simulation/introduction.html).

Before doing anything with simulation, make sure desktop support is turned on. Follow [these instructions](https://docs.wpilib.org/en/stable/docs/software/wpilib-tools/robot-simulation/introduction.html).

WPILIB contains generic simulation classes for different mechanisms (like `ElevatorSim`) based on physical details and constraints about your system. You can see a full list of them and examples on using them [here](https://docs.wpilib.org/en/stable/docs/software/wpilib-tools/robot-simulation/physics-sim.html).


