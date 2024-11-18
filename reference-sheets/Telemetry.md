# Telemetry

### The art of logging and log-viewing

In testing (real or simulated), it is common to want to directly observe robot measurements and values in order to tune your systems and debug. Rather than looping print statements, WPILib provides interfaces allowing certain information to be logged while the robot runs.

Loggers send data to [NetworkTables](https://docs.wpilib.org/en/stable/docs/software/networktables/networktables-intro.html), which can be read [while running](#dashboards) or stored for later viewing in [log files](#log-viewers).

Only classes that implement `Sendable` can be sent over NetworkTables; see [here](https://docs.wpilib.org/en/stable/docs/software/telemetry/robot-telemetry-with-sendable.html#what-is-sendable) for more details.

For more in-depth information on the inner workings, visit [the docs](https://docs.wpilib.org/en/stable/docs/software/telemetry/telemetry.html).

## Logging libraries

Logging libraries, third-party or WPILib-made, are not monolithic. Some are annotation-based (using Java `@Annotations`), while others are framework-based. All are unique; a nice list of them can be found [here](https://docs.wpilib.org/en/stable/docs/software/telemetry/3rd-party-libraries.html).

- [Monologue](https://github.com/shueja/Monologue/wiki) (we use this!)
- [Epilogue](https://docs.wpilib.org/pt/latest/docs/software/telemetry/robot-telemetry-with-annotations.html) (official WPILib)
- [AdvantageKit](https://github.com/Mechanical-Advantage/AdvantageKit/blob/main/docs/WHAT-IS-ADVANTAGEKIT.md)
- [URCL](https://github.com/Mechanical-Advantage/URCL)

## Dashboards

There are two types of dashboards: driving and programming. We'll be talking about the ones related to debugging.

These programs allow you to view data over NetworkTables in real time, allowing you to see logged data while working on a real or simulated robot. These **will be your main tools for debugging**.

Here's a [nice list](https://docs.wpilib.org/en/stable/docs/software/dashboards/dashboard-intro.html) of them.

## Log Viewers

Log viewers will pull measurements from log files and most commonly allow you to graph data or visualize them in some way. These are especially useful for direct post-match debugging, given you have the ability to process and debug with the data formats.

See [this doc](https://docs.wpilib.org/en/stable/docs/software/telemetry/datalog-download.html#downloading-processing-data-logs) for more information.