# Introduction

In this guide, we're going to be making a tic tac toe game, and learning important Java concepts as we go.
## Prerequisites

## Goals

Familiarity with the following:
- Enums
- Records
- JUnit testing

Also, a working tic tac toe game!
## Best Practices

See [Java101](Java101.md#best-practices).
## Setup

If you did [Java101](Java101.md) and 102, use the same repository that you used there. Otherwise, follow the [instructions in Java101 to set up a repository](Java101.md#setup). 

Make a new directory called `tic-tac-toe`. We'll be working in that directory. Make a file in `tic-tac-toe` called `Main.java`, as well as a `README.md` file.

In the README, link [this guide](/projects/intro-to-programming/tic-tac-toe).
## Board

First off, we're going to make the tic tac toe board. We did something similar in Java101 (LINK), where we made a three by three 2D array, and called it a board. Now, we're going to make a `Board` class, from which we will be able to create `Board` objects. Our board class will contain a few things:
- the `board`: a three by three 2D integer array. It will start out with only 0s, because all squares start out blank.
- a `move` method: a method that takes a move (which player's turn it is and where they want to go) and updates the board to reflect the new turn
- an `winner` method: a method that takes no inputs, and returns who (if anyone) has won the game.
- an `over` method: a method that takes no inputs and returns whether or not the game is over.
- a `toString` method

We will not write our own constructor, because we don't need any input to customize each board. When first created, every board should look the same. It is only as the game goes on and players take turns that board become more unique. When you don't add a constructor, instead there is a *default constructor*. Default constructors take no inputs, and simply return a new object of that class.

```java
public class Board {
	private final int[][] board = new int[3][3];
}
```

Okay, next let's add our `toString` method. Let's try to make something that looks like this:
```
x - -
- o x
- - -
```

First off, let's make a method to convert integers that represent players ($0$, $-1$, $1$):

```java
private static String playerToString(int player) {
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

This is private because it is only used inside of the class, and static because it doesn't have anything to do with a particular `Board`. I did something here that we haven't done before: I threw an exception. Theoretically, someone could pass this method an integer that is not 1 or -1 or 0, and if that happens, we know that something has gone wrong. So we throw an exception (an error), and that will stop everything and show us our message.

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

Next up, let's write our `move` method. This method needs to take what player is playing and which row and column they want to move in. Here's the header:

```java
public void move(int player, int row, int column);
```

Try to fill in the function. To start, write something that just fills in the board.

