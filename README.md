# Introduction

This project simulates the coexistence of two species: Doves and Hawks. Each day, Doves and Hawks are randomly paired into couples where they must decide whether to share the food or not. The simulation allows you to define the rules for sharing or stealing food, as well as control various environmental parameters.

## Libraries Used

### 1. Matplotlib
[Matplotlib](https://matplotlib.org/) is a comprehensive library for creating static, animated, and interactive visualizations in Python. It is particularly useful for plotting graphs and charts, such as line plots, bar charts, scatter plots, and pie charts. The library is highly customizable, allowing for fine-tuning of visual elements to create publication-quality figures.

### 2. Tkinter
[Tkinter](https://docs.python.org/3/library/tkinter.html) is the standard Python interface to the Tk GUI toolkit. It is a powerful tool for creating graphical user interfaces (GUIs) in Python applications. Tkinter is easy to use and provides a variety of widgets, including buttons, labels, text boxes, and more, enabling the creation of complex and interactive applications.

### 3. Random
The [random](https://docs.python.org/3/library/random.html) module in Python implements pseudo-random number generators for various distributions. It is useful for generating random numbers, making random selections, shuffling sequences, and other tasks that require randomness. The module is often used in simulations, games, and testing scenarios.

### 4. Enum
The [enum](https://docs.python.org/3/library/enum.html) module in Python provides support for creating enumerations, which are a set of symbolic names bound to unique, constant values. Enums are used to represent fixed sets of related values, improving code readability and maintainability by providing meaningful names instead of arbitrary numbers or strings.

## Usage
These libraries are employed in the project to create visual representations of data (Matplotlib), build a user-friendly interface (Tkinter), generate random data for simulations (random), and define fixed sets of values (Enum). Together, they enable the creation of a comprehensive application with a graphical interface, data visualization, and structured code.

# Input

## Food Pairs
In each iteration, a certain number of food pairs spawn. Each food pair equals 2 points:
- 1 point is needed for a creature to survive.
- 2 points are needed for a creature to reproduce.

The probability of survival and reproduction is based on the amount of food received:
- If a creature receives 1.5 food points, it has a 100% chance of surviving and a 50% chance of reproducing.
- If a creature receives 0.2 food points, it has a 20% chance of surviving and a 0% chance of reproducing.

## Interaction Rules Table
The following table outlines how much food each creature will receive after an encounter:

|       | Dove | Hawk |
|-------|------|------|
| **Dove** |  1  | 1/2  |
| **Hawk** | 3/2  |  0  |

- **Dove vs. Dove**: Both doves share the food equally, each receiving 1 point.
- **Dove vs. Hawk**: The hawk receive 1 point and steals 1/2 point, leaving the dove with 1/2 point.
- **Hawk vs. Hawk**: Both hawks lose all energy fighting and receive 0 points.

## Initial Dove and Hawk Counts
The number of doves and hawks that will be present at the beginning of the simulation.

## Iterations to Run
The number of iterations during which creatures will meet and interact with one another.

# Credit
Inspired by 

<div align="center">
  <iframe width="560" height="315" src="https://www.youtube.com/embed/YNMkADpvO4w" frameborder="0" allow="accelerometer; autoplay; encrypted-media; gyroscope; picture-in-picture" allowfullscreen></iframe>
</div>
