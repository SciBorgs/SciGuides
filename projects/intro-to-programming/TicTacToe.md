# Introduction

In this guide, we're going to be making a tic tac toe game, and learning important Java concepts as we go.
## Prerequisites

- Java101
- Java102
- Java103
- Unit Testing with JUnit (make guide
	- Extension installed
- etc
## Goals

Familiarity with the following:
- Enums
- Records
- JUnit testing

Also, a working tic tac toe game!
## Best Practices

See [Java101](Java101.md#best-practices).
## Setup

If you did [Java101](/projects/intro-to-programming/Java101.md) and [Java102](/projects/intro-to-programming/Java102.md), use the same repository that you used there. Otherwise, follow the [instructions in Java101 to set up a repository](Java101.md#setup).

Make a new directory called `tictactoe` (or if you're making a whole new repository, just call it tic-tac-toe). We'll be working in that directory/package. Every Java file of `tictactoe` should  start with the line `package tictactoe;`. Make a file in `tictactoe` called `Main.java`, as well as a `README.md` file.

In the README, link [this guide](/projects/intro-to-programming/TicTacToe.md).

(Press on the testing tab -- test tube -- on the left side of the VSCode window.) Click "Enable Java Tests". At the top of the screen, press "JUnit Jupiter".
# Board

First off, we're going to make the tic tac toe board. We did something similar in [Java101](/projects/intro-to-programming/Java101.md#2d-arrays), where we made a three by three 2D array, and called it a board. Now, we're going to make a `Board` class, from which we will be able to create `Board` objects. Our board class will contain a few things:
- the `board`: a three by three 2D integer array. It will start out with only 0s, because all squares start out blank.
- a `get` method: a method that takes a row and column and returns the contents of that place
- a `move` method: a method that takes a move (which player's turn it is and where they want to go) and updates the board to reflect the new turn
- an `winner` method: a method that takes no inputs, and returns who (if anyone) has won the game.
- an `over` method: a method that takes no inputs and returns whether or not the game is over.
- a `toString` method

We will not write our own constructor, because we don't need any input to customize each board. When first created, every board should look the same. It is only as the game goes on and players take turns that board become more unique. When you don't add a constructor, instead there is a *default constructor*. Default constructors take no inputs, and simply return a new object of that class.

```java
package tictactoe;

public class Board {
	private final int[][] board = new int[3][3];
}
```
## toString

Okay, next let's add our `toString` method. Let's try to make our board look like this:

```
x - -
- o x
- - -
```

First off, let's make a method to convert integers that represent players ($0$, $-1$, $1$) to strings:

```java
public static String playerToString(int player) {
	if (player == -1) {
		return "o";
	} else if (player == 0) {
		return "-";
	} else if (player == 1) {
		return "x";
	} else {
		throw new RuntimeException("not a valid player: " + player);
	}
}
```

This is static because it doesn't have anything to do with a particular `Board`. I did something here that we haven't done before: I threw an exception. Theoretically, someone could pass this method an integer that is not 1 or -1 or 0, and if that happens, we know that something has gone wrong. So we throw an exception (an error), and that will stop everything and show us our message.

Now let's write our `toString` method:

```java
@Override
public String toString() {
	String str = "";
	for (int[] row : board) {
		for (int square : row) {
			str += playerToString(square) + " ";
		}
		str += "\n";
	}
	return str;
}
```

As always, go through this method and make sure you really understand all of it.

Now, before we write anything else in this class, let's test what we've done so far.

### Testing

So far in the intro to programming series, we've tested our code by printing values and checking if they are what we expected. For this guide, our code is getting a little more complicated, and we're going to start using Unit Tests!

Make a new directory inside of `tictactoe` called `test`. Inside of `test`, make a file called `BoardTest.java`.  Import JUnit assertions. Here's what your file should look like:
```java
package tictactoe.test;

import static org.junit.jupiter.api.Assertions.*;
import org.junit.Test;

public class BoardTest {
}
```

Let's add a test to make sure that our `playerToString` works! We'll have four test cases: `playerToString(1)`, `playerToString(-1)`, `playerToString(0)`, and  `playerToString(2)`. The first three cases should give us "x", "o", and "-" respectively. The last case, `playerToString(2)`, should cause an exception to be thrown. Here's how we would write a test to verify those expectations:

```java
@Test
public void playerToString() {
        assertEquals("x", Board.playerToString(1));
        assertEquals("o", Board.playerToString(-1));
        assertEquals("-", Board.playerToString(0));
        assertThrows(RuntimeException.class, () -> Board.playerToString(2));
}
```

The first three assertions are pretty intuitive. The last one is a little more complicated. Essentially, it's asserting that when the code `Board.playerToString(2)` is run, a `RuntimeException` will be thrown. I'm not going to explain the `() ->` notation here, but it will become important in future projects. If you want to learn more now, read [this](link).

Now run the test and see if it works!

Next, let's test our whole `toString` method. If we take an empty board and turn it into a String, we should expect to get back the following: `"- - - \n- - - \n- - - \n"`

```java
@Test
public void boardToString() {
	assertEquals("- - - \n- - - \n- - - \n", new Board().toString());
}
```

Run it to check if it works!
## get & move

Let's write a super simple method to get the contents of a place:

```java
public int get(int row, int column) {
	return board[row][column];
}
```


Next up is our `move` method. This method needs to take what player is playing and which row and column they want to move in. Here's the header:

```java
public void move(int player, int row, int column);
```

Try to fill in the function. To start, write something that just inserts `player` at the specified `row` and `column` of `board`. Then, in `BoardTest`, write something like the following to test your function:

```java
@Test
public void testMove() {
	Board b = new Board;
	b.move(1, 2, 0);
	assertEquals(1, b.get(2, 0));
	b.move(-1, 1, 1);
	assertEquals(-1, b.get(1, 1));
}
```

Once you have that test working, update your `move` function so that it doesn't allow invalid moves. It should pass this updated version of `testMove`:

```java
@Test
public void testMove() {
	Board b = new Board;
	b.move(1, 2, 0);
	assertEquals(1, b.get(2, 0));
	b.move(-1, 1, 1);
	assertEquals(-1, b.get(1, 1));
	// check that you can't play in a space that's full already
	assertThrows(RuntimeException.class, () -> b.move(-1, 2, 0));
	// check that you can't give an int other than 1 or -1 as player
	assertThrows(RuntimeException.class, () -> b.move(0, 2, 2));
}
```

## winner

The next step is to write a method that finds the winner of a board. This method will return `1` if `x` has won the board, `-1` if y has won, and `0` if no one has won. I'm going to write some of the code for you. Fill the rest in.

```java
public int winner() {
	
}
```