# Fallibles

Currently our implementation (heavily based on 3015's) looks like this:

```java
public record HardwareFault(String description, double timestamp, boolean isWarning) implements Sendable {}

@FunctionalInterface
public interface Fallible {
  public List<HardwareFault> getFaults();
}
```

Note that we don't really use the warning and timestamp attributes in our setup.

In order to make the creation of faults ergonomic, we use a `FaultBuilder`, resulting in boilerplate like this

```java
// Arm.java, 2023 robot code
@Override
public List<HardwareFault> getFaults() {
return FaultBuilder.create()
    .register(elevator.getFaults())
    .register(elbow.getFaults())
    .register(wrist.getFaults())
    .build();
}
```

There are many issues with this system:

- specific individual faults cannot be easily checked, beyond triggers

^ the main issue

## Improvements

Rust/ml Result union types can more effectively account for (no error) U ([any of the following errors])

```java
public sealed interface Result<T, E> {
  public final class Ok<T> implements Result<T> {}
  public final record Error<T>(T value) implements Result<T> {}
}
```

From there, subsystems could directly deal with internal faults, perhaps exporting their own

```java
@FunctionalInterface
public interface Fallible {
  public List<Error> getFaults();
}
```

Defining custom errors is slightly annoying

```java
public sealed interface MyCustomError {

}

Result<MyCustomError>
```
