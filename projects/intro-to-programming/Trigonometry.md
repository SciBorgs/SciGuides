# Introduction
This is meant for you if you are unfamiliar with trig functions. This will not cover all of trig in depth, but enough of which is needed for [Java102](Java102.md#challenge-rotation). 

## Prerequisites
- [Algebra 1](https://www.khanacademy.org/math/algebra) - understanding of functions, cartesian coordinate grid
- [Basic geometry](https://www.khanacademy.org/math/geometry) - understanding of angles

# Radians
You are probably most familiar with angles being measured in degrees, where a right angle is 90°, and a full circle is 360°.
However, the unit of degrees is arbitrary. Why should a degree be 1/360 of a circle, and not 1/180, or 1/2?

Angles can also be measured in radians. Similar to how speed can be measured in miles per hour or meters per second, radians are another unit for angles.

A radian is the angle created when the radius of a circle is wrapped around the circumference.

![Diagram of radian (https://www.mathsisfun.com/geometry/radians.html)](https://www.mathsisfun.com/geometry/images/radian-circle.svg)

If you know the formula for the circumference of a circle ($C = 2πr$), then you can see that a full circle is 2π radians (when you divide the circumference by its radius). So 360° = 2π rad. Radians is abbreviated to rad. The radius of the circle does not matter. 

## Converting Degrees to Radians
With the equation 360° = 2π rad, you can convert between degrees and radians:
$1° = \frac{π}{180}\hspace{0.1cm} rad$, or $1 \hspace{0.1cm}rad = \frac{180}{π}°$

There also exists a conversion method in Java, so you don't have to type out all the calculations:
```java
Math.toDegrees(angle); // angle is in radians, and the output is degrees
Math.toRadians(angle); // angle is in degrees, and the output is radians
```

# Angles in Right Triangles
We know that a right triangle is defined by a triangle containing a right angle (90° or (π/2) rad). If you know one of the other angles of the triangle, then you know all 3 angles (ex. if you know that a right triangle contains a 50° angle, you know the missing angle is 40°, since the interior angles of all triangles sum to 180°).

A property that's more obvious in right triangles is that you can find the ratio of a leg of a triangle over its hypotenuse as long as you know an angle (that's not the right angle) of the triangle. [This](https://services.math.duke.edu/~rann/labs106.2018pdfs/Lab1.A.Crash.Course.in.Trig.pdf) helps explain why this is the case.

So as long as you know an angle of the right triangle, and a side length, you can find the lengths of each side, and the angles of each vertex.

The trigonometric functions take the angle as the input, and output specific ratios ($θ$ represents an angle):

- $sin(θ) = \frac{leg\hspace{0.1cm}opposite \hspace{0.1cm}of \hspace{0.1cm}angle}{hypotenuse}$ - written as sine
- $cos(θ) = \frac{leg \hspace{0.1cm}adjacent (next) \hspace{0.1cm}to \hspace{0.1cm}angle}{hypotenuse}$ - written as cosine
- $tan(θ) = \frac{leg \hspace{0.1cm}opposite \hspace{0.1cm}of \hspace{0.1cm}angle}{leg \hspace{0.1cm}adjacent\hspace{0.1cm} to \hspace{0.1cm}angle}$ also equal to $\frac{sin(θ)}{cos(θ)}$ - written as tangent

if you multiply $sin(θ)$ and the $cos(θ)$ by the hypotenuse, you'd get the length of the leg opposite of $θ$ and the length of the leg adjacent to θ respectively.

## Code Representation
In Java, the `Math` library has methods for these trig functions:

```java
Math.cos(angle);
Math.sin(angle);
Math.tan(angle);
```
Keep in mind that these functions take in **radians**. 
# Inverse Trig Functions
There are also the inverse trig functions, where if you input the ratio of the leg opposite of an unknown angle $θ$ over the hypotenuse of the triangle, the output is the angle:

- $sin^{-1}(\frac{leg \hspace{0.1cm}opposite \hspace{0.1cm}θ}{hypotenuse}) = θ$ - written out as arcsine
- $cos^{-1}(\frac{leg \hspace{0.1cm}adjacent\hspace{0.1cm} θ}{hypotenuse}) = θ$ - written out as arccosine
- $tan^{-1}(\frac{leg \hspace{0.1cm}opposite\hspace{0.1cm} θ}{leg \hspace{0.1cm}adjacent \hspace{0.1cm}θ}) = θ$ - written out as arctangent

The output of the inverse of a function applied to an output of the original function results in the input value of the original function. In a more comprehensible form:

- $sin^{-1}(sin(θ)) = θ$

In Java, the inverse functions are written like this:
```java
Math.asin(ratio);
Math.acos(ratio);
Math.atan(ratio);
```
Also, keep in mind that these methods output **radians**.