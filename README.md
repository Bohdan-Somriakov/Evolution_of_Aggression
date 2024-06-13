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

## Matplotlib installation

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
| Dove |  1  | 1/2  |
| Hawk | 3/2  |  0  |

- **Dove vs. Dove**: Both doves share the food equally, each receiving 1 point.
- **Dove vs. Hawk**: The hawk receive 1 point and steals 1/2 point, leaving the dove with 1/2 point.
- **Hawk vs. Hawk**: Both hawks lose all energy fighting and receive 0 points.

## Initial Dove and Hawk Counts
The number of doves and hawks that will be present at the beginning of the simulation.

## Iterations to Run
The number of iterations during which creatures will meet and interact with one another.

# Results

## Typical behaviour

In habitats where Hawks are abundant, adopting a Dove strategy is advantageous. The prevalent Hawk-Hawk conflicts create opportunities for Doves to obtain food with minimal risk, resulting in a consistent gain of 0.5 food units per interaction.

Conversely, in environments where Doves outnumber Hawks, transitioning to a Hawk strategy becomes beneficial. With reduced competition from Doves, Hawks can secure a more substantial 1.5 food units per encounter.

<p align="center">
  <img src="https://github.com/Bohdan-Somriakov/Evolution_of_Aggression/blob/main/examples/example1/data.png" alt="Image" style="display:block; margin:auto; width:300px;"/>
</p>

<p align="center">
  <img src="https://github.com/Bohdan-Somriakov/Evolution_of_Aggression/blob/main/examples/example1/population_simulation_graph.png" alt="Image" style="display:block; margin:auto;"/>
</p>

<p align="center">
  <img src="https://github.com/Bohdan-Somriakov/Evolution_of_Aggression/blob/main/examples/example1/population_simulation_plots.png" alt="Image" style="display:block; margin:auto;"/>
</p>

<p align="center">
  <img src="https://github.com/Bohdan-Somriakov/Evolution_of_Aggression/blob/main/examples/example1/population_simulation_hist.png" alt="Image" style="display:block; margin:auto;"/>
</p>

<p align="center">
  <img src="https://github.com/Bohdan-Somriakov/Evolution_of_Aggression/blob/main/examples/example1/population_simulation_pie.png" alt="Image" style="display:block; margin:auto; width:400px;"/>
</p>

<p align="center">
  <img src="https://github.com/Bohdan-Somriakov/Evolution_of_Aggression/blob/main/examples/example1/population_simulation_pies.png" alt="Image" style="display:block; margin:auto;"/>
</p>

Both strategies demonstrate survival, indicating their effectiveness in different scenarios.

## Doves only

In doves only scenerio Doves do not have any competitors.

<p align="center">
  <img src="https://github.com/Bohdan-Somriakov/Evolution_of_Aggression/blob/main/examples/example2/data.png" alt="Image" style="display:block; margin:auto; width:300px;"/>
</p>

<p align="center">
  <img src="https://github.com/Bohdan-Somriakov/Evolution_of_Aggression/blob/main/examples/example2/population_simulation_graph.png" alt="Image" style="display:block; margin:auto;"/>
</p>

<p align="center">
  <img src="https://github.com/Bohdan-Somriakov/Evolution_of_Aggression/blob/main/examples/example2/population_simulation_plots.png" alt="Image" style="display:block; margin:auto;"/>
</p>

<p align="center">
  <img src="https://github.com/Bohdan-Somriakov/Evolution_of_Aggression/blob/main/examples/example2/population_simulation_hist.png" alt="Image" style="display:block; margin:auto;"/>
</p>

<p align="center">
  <img src="https://github.com/Bohdan-Somriakov/Evolution_of_Aggression/blob/main/examples/example2/population_simulation_pie.png" alt="Image" style="display:block; margin:auto; width:400px;"/>
</p>

<p align="center">
  <img src="https://github.com/Bohdan-Somriakov/Evolution_of_Aggression/blob/main/examples/example2/population_simulation_pies.png" alt="Image" style="display:block; margin:auto;"/>
</p>

In this observation, the life of Doves appears significantly better compared to the coexistence of Doves and Hawks. The absence of aggression among Hawks contributed to a more peaceful environment for Doves.

## Hawks only

In hawks only scenerio Hawks do not have any competitors.

<p align="center">
  <img src="https://github.com/Bohdan-Somriakov/Evolution_of_Aggression/blob/main/examples/example3/data.png" alt="Image" style="display:block; margin:auto; width:300px;"/>
</p>

<p align="center">
  <img src="https://github.com/Bohdan-Somriakov/Evolution_of_Aggression/blob/main/examples/example3/population_simulation_graph.png" alt="Image" style="display:block; margin:auto;"/>
</p>

<p align="center">
  <img src="https://github.com/Bohdan-Somriakov/Evolution_of_Aggression/blob/main/examples/example3/population_simulation_plots.png" alt="Image" style="display:block; margin:auto;"/>
</p>

<p align="center">
  <img src="https://github.com/Bohdan-Somriakov/Evolution_of_Aggression/blob/main/examples/example3/population_simulation_hist.png" alt="Image" style="display:block; margin:auto;"/>
</p>

<p align="center">
  <img src="https://github.com/Bohdan-Somriakov/Evolution_of_Aggression/blob/main/examples/example3/population_simulation_pie.png" alt="Image" style="display:block; margin:auto; width:400px;"/>
</p>

<p align="center">
  <img src="https://github.com/Bohdan-Somriakov/Evolution_of_Aggression/blob/main/examples/example3/population_simulation_pies.png" alt="Image" style="display:block; margin:auto;"/>
</p>

Hawks resorted to slaughtering each other as soon as they ate all free food supply, highlighting their inability to survive without the presence of Doves.

## Dove among Hawks 

1 Dove surrounded by Hawks.

<p align="center">
  <img src="https://github.com/Bohdan-Somriakov/Evolution_of_Aggression/blob/main/examples/example4/data.png" alt="Image" style="display:block; margin:auto; width:300px;"/>
</p>

<p align="center">
  <img src="https://github.com/Bohdan-Somriakov/Evolution_of_Aggression/blob/main/examples/example4/population_simulation_graph.png" alt="Image" style="display:block; margin:auto;"/>
</p>

<p align="center">
  <img src="https://github.com/Bohdan-Somriakov/Evolution_of_Aggression/blob/main/examples/example4/population_simulation_plots.png" alt="Image" style="display:block; margin:auto;"/>
</p>

<p align="center">
  <img src="https://github.com/Bohdan-Somriakov/Evolution_of_Aggression/blob/main/examples/example4/population_simulation_hist.png" alt="Image" style="display:block; margin:auto;"/>
</p>

<p align="center">
  <img src="https://github.com/Bohdan-Somriakov/Evolution_of_Aggression/blob/main/examples/example4/population_simulation_pie.png" alt="Image" style="display:block; margin:auto; width:400px;"/>
</p>

<p align="center">
  <img src="https://github.com/Bohdan-Somriakov/Evolution_of_Aggression/blob/main/examples/example4/population_simulation_pies.png" alt="Image" style="display:block; margin:auto;"/>
</p>

Hawks immediately resorted to slaughtering each other, while Doves seized this opportunity to reproduce and ensure their survival.

## Hawk among Doves 

1 Hawk surrounded by Doves.

<p align="center">
  <img src="https://github.com/Bohdan-Somriakov/Evolution_of_Aggression/blob/main/examples/example5/data.png" alt="Image" style="display:block; margin:auto; width:300px;"/>
</p>

<p align="center">
  <img src="https://github.com/Bohdan-Somriakov/Evolution_of_Aggression/blob/main/examples/example5/population_simulation_graph.png" alt="Image" style="display:block; margin:auto;"/>
</p>

<p align="center">
  <img src="https://github.com/Bohdan-Somriakov/Evolution_of_Aggression/blob/main/examples/example5/population_simulation_plots.png" alt="Image" style="display:block; margin:auto;"/>
</p>

<p align="center">
  <img src="https://github.com/Bohdan-Somriakov/Evolution_of_Aggression/blob/main/examples/example5/population_simulation_hist.png" alt="Image" style="display:block; margin:auto;"/>
</p>

<p align="center">
  <img src="https://github.com/Bohdan-Somriakov/Evolution_of_Aggression/blob/main/examples/example5/population_simulation_pie.png" alt="Image" style="display:block; margin:auto; width:400px;"/>
</p>

<p align="center">
  <img src="https://github.com/Bohdan-Somriakov/Evolution_of_Aggression/blob/main/examples/example5/population_simulation_pies.png" alt="Image" style="display:block; margin:auto;"/>
</p>

The overall habitat flourished initially. However, with Hawks reproducing and subsequently decreasing the average population by approximately 30% due to their aggressive tendencies, the ecosystem faced a decline.

## Large scale

The same experiment conducted on a larger scale.

<p align="center">
  <img src="https://github.com/Bohdan-Somriakov/Evolution_of_Aggression/blob/main/examples/example6/data.png" alt="Image" style="display:block; margin:auto; width:300px;"/>
</p>

<p align="center">
  <img src="https://github.com/Bohdan-Somriakov/Evolution_of_Aggression/blob/main/examples/example6/population_simulation_graph.png" alt="Image" style="display:block; margin:auto;"/>
</p>

<p align="center">
  <img src="https://github.com/Bohdan-Somriakov/Evolution_of_Aggression/blob/main/examples/example6/population_simulation_plots.png" alt="Image" style="display:block; margin:auto;"/>
</p>

<p align="center">
  <img src="https://github.com/Bohdan-Somriakov/Evolution_of_Aggression/blob/main/examples/example6/population_simulation_hist.png" alt="Image" style="display:block; margin:auto;"/>
</p>

<p align="center">
  <img src="https://github.com/Bohdan-Somriakov/Evolution_of_Aggression/blob/main/examples/example6/population_simulation_pie.png" alt="Image" style="display:block; margin:auto; width:400px;"/>
</p>

<p align="center">
  <img src="https://github.com/Bohdan-Somriakov/Evolution_of_Aggression/blob/main/examples/example6/population_simulation_pies.png" alt="Image" style="display:block; margin:auto;"/>
</p>

The results are very stable.

## Small scale hawk problem

Only 10 food pairs.

<p align="center">
  <img src="https://github.com/Bohdan-Somriakov/Evolution_of_Aggression/blob/main/examples/example7/data.png" alt="Image" style="display:block; margin:auto; width:300px;"/>
</p>

<p align="center">
  <img src="https://github.com/Bohdan-Somriakov/Evolution_of_Aggression/blob/main/examples/example7/population_simulation_graph.png" alt="Image" style="display:block; margin:auto;"/>
</p>

<p align="center">
  <img src="https://github.com/Bohdan-Somriakov/Evolution_of_Aggression/blob/main/examples/example7/population_simulation_plots.png" alt="Image" style="display:block; margin:auto;"/>
</p>

<p align="center">
  <img src="https://github.com/Bohdan-Somriakov/Evolution_of_Aggression/blob/main/examples/example7/population_simulation_hist.png" alt="Image" style="display:block; margin:auto;"/>
</p>

<p align="center">
  <img src="https://github.com/Bohdan-Somriakov/Evolution_of_Aggression/blob/main/examples/example7/population_simulation_pie.png" alt="Image" style="display:block; margin:auto; width:400px;"/>
</p>

<p align="center">
  <img src="https://github.com/Bohdan-Somriakov/Evolution_of_Aggression/blob/main/examples/example7/population_simulation_pies.png" alt="Image" style="display:block; margin:auto;"/>
</p>

Scarcity of food leads to a decrease in the overall population of creatures. With a small number of Hawks, the probability of their encounters increases significantly. In an unfortunate turn of events, all Hawks ended up meeting and ultimately eliminating each other, leaving only Doves remaining. The higher the number of iterations, the greater the likelihood of such an outcome.

## Small scale dove problem

Only 5 food pairs.

<p align="center">
  <img src="https://github.com/Bohdan-Somriakov/Evolution_of_Aggression/blob/main/examples/example8/data.png" alt="Image" style="display:block; margin:auto; width:300px;"/>
</p>

<p align="center">
  <img src="https://github.com/Bohdan-Somriakov/Evolution_of_Aggression/blob/main/examples/example8/population_simulation_graph.png" alt="Image" style="display:block; margin:auto;"/>
</p>

<p align="center">
  <img src="https://github.com/Bohdan-Somriakov/Evolution_of_Aggression/blob/main/examples/example8/population_simulation_plots.png" alt="Image" style="display:block; margin:auto;"/>
</p>

<p align="center">
  <img src="https://github.com/Bohdan-Somriakov/Evolution_of_Aggression/blob/main/examples/example8/population_simulation_hist.png" alt="Image" style="display:block; margin:auto;"/>
</p>

<p align="center">
  <img src="https://github.com/Bohdan-Somriakov/Evolution_of_Aggression/blob/main/examples/example8/population_simulation_pie.png" alt="Image" style="display:block; margin:auto; width:400px;"/>
</p>

<p align="center">
  <img src="https://github.com/Bohdan-Somriakov/Evolution_of_Aggression/blob/main/examples/example8/population_simulation_pies.png" alt="Image" style="display:block; margin:auto;"/>
</p>

Scarcity of food leads to a decrease in the overall population of creatures. With a small number of Doves, the probability of their encounters with Hawks increases significantly. In an unfortunate turn of events, all Hawks ended up meeting and ultimately eliminating all Doves, leaving only Hawks remaining. Subsequently, the Hawks turned on each other, resulting in further slaughter within their own ranks. The higher the number of iterations, the greater the likelihood of such an outcome.

## Hawks coop with each other

New table: 

|       | Dove | Hawk |
|-------|------|------|
| Dove |  1  | 1/2  |
| Hawk | 3/2  |  **1**  |

<p align="center">
  <img src="https://github.com/Bohdan-Somriakov/Evolution_of_Aggression/blob/main/examples/example9/data.png" alt="Image" style="display:block; margin:auto; width:300px;"/>
</p>

<p align="center">
  <img src="https://github.com/Bohdan-Somriakov/Evolution_of_Aggression/blob/main/examples/example9/population_simulation_graph.png" alt="Image" style="display:block; margin:auto;"/>
</p>

<p align="center">
  <img src="https://github.com/Bohdan-Somriakov/Evolution_of_Aggression/blob/main/examples/example9/population_simulation_plots.png" alt="Image" style="display:block; margin:auto;"/>
</p>

<p align="center">
  <img src="https://github.com/Bohdan-Somriakov/Evolution_of_Aggression/blob/main/examples/example9/population_simulation_hist.png" alt="Image" style="display:block; margin:auto;"/>
</p>

<p align="center">
  <img src="https://github.com/Bohdan-Somriakov/Evolution_of_Aggression/blob/main/examples/example9/population_simulation_pie.png" alt="Image" style="display:block; margin:auto; width:400px;"/>
</p>

<p align="center">
  <img src="https://github.com/Bohdan-Somriakov/Evolution_of_Aggression/blob/main/examples/example9/population_simulation_pies.png" alt="Image" style="display:block; margin:auto;"/>
</p>

Hawks shared food among themselves but engaged in fierce competition with Doves for the remaining food, ultimately leading to the Hawks eliminating all the Doves.

## Hawks coop with each other (1 Hawk)

New table: 

|       | Dove | Hawk |
|-------|------|------|
| Dove |  1  | 1/2  |
| Hawk | 3/2  |  **1**  |

Start with 1 Hawk.

<p align="center">
  <img src="https://github.com/Bohdan-Somriakov/Evolution_of_Aggression/blob/main/examples/example10/data.png" alt="Image" style="display:block; margin:auto; width:300px;"/>
</p>

<p align="center">
  <img src="https://github.com/Bohdan-Somriakov/Evolution_of_Aggression/blob/main/examples/example10/population_simulation_graph.png" alt="Image" style="display:block; margin:auto;"/>
</p>

<p align="center">
  <img src="https://github.com/Bohdan-Somriakov/Evolution_of_Aggression/blob/main/examples/example10/population_simulation_plots.png" alt="Image" style="display:block; margin:auto;"/>
</p>

<p align="center">
  <img src="https://github.com/Bohdan-Somriakov/Evolution_of_Aggression/blob/main/examples/example10/population_simulation_hist.png" alt="Image" style="display:block; margin:auto;"/>
</p>

<p align="center">
  <img src="https://github.com/Bohdan-Somriakov/Evolution_of_Aggression/blob/main/examples/example10/population_simulation_pie.png" alt="Image" style="display:block; margin:auto; width:400px;"/>
</p>

<p align="center">
  <img src="https://github.com/Bohdan-Somriakov/Evolution_of_Aggression/blob/main/examples/example10/population_simulation_pies.png" alt="Image" style="display:block; margin:auto;"/>
</p>

Hawks shared food among themselves but engaged in fierce competition with Doves for the remaining food, ultimately leading to the Hawks eliminating all the Doves, despite starting with only 1 Hawk.

## 2 Hawks get at least something

New table: 

|       | Dove | Hawk |
|-------|------|------|
| Dove |  1  | 1/2  |
| Hawk | 3/2  |  **1/2**  |

Instead of wasting all their energy and dying, two Hawks would end up going home with 1/2 of the food each.

<p align="center">
  <img src="https://github.com/Bohdan-Somriakov/Evolution_of_Aggression/blob/main/examples/example11/data.png" alt="Image" style="display:block; margin:auto; width:300px;"/>
</p>

<p align="center">
  <img src="https://github.com/Bohdan-Somriakov/Evolution_of_Aggression/blob/main/examples/example11/population_simulation_graph.png" alt="Image" style="display:block; margin:auto;"/>
</p>

<p align="center">
  <img src="https://github.com/Bohdan-Somriakov/Evolution_of_Aggression/blob/main/examples/example11/population_simulation_plots.png" alt="Image" style="display:block; margin:auto;"/>
</p>

<p align="center">
  <img src="https://github.com/Bohdan-Somriakov/Evolution_of_Aggression/blob/main/examples/example11/population_simulation_hist.png" alt="Image" style="display:block; margin:auto;"/>
</p>

<p align="center">
  <img src="https://github.com/Bohdan-Somriakov/Evolution_of_Aggression/blob/main/examples/example11/population_simulation_pie.png" alt="Image" style="display:block; margin:auto; width:400px;"/>
</p>

<p align="center">
  <img src="https://github.com/Bohdan-Somriakov/Evolution_of_Aggression/blob/main/examples/example11/population_simulation_pies.png" alt="Image" style="display:block; margin:auto;"/>
</p>

Hawks grew significantly stronger.

## 2 Hawks get at least something (large scale)

New table: 

|       | Dove | Hawk |
|-------|------|------|
| Dove |  1  | 1/2  |
| Hawk | 3/2  |  **1/2**  |

Instead of wasting all their energy and dying, two Hawks would end up going home with 1/2 of the food each.
Large scale.

<p align="center">
  <img src="https://github.com/Bohdan-Somriakov/Evolution_of_Aggression/blob/main/examples/example12/data.png" alt="Image" style="display:block; margin:auto; width:300px;"/>
</p>

<p align="center">
  <img src="https://github.com/Bohdan-Somriakov/Evolution_of_Aggression/blob/main/examples/example12/population_simulation_graph.png" alt="Image" style="display:block; margin:auto;"/>
</p>

<p align="center">
  <img src="https://github.com/Bohdan-Somriakov/Evolution_of_Aggression/blob/main/examples/example12/population_simulation_plots.png" alt="Image" style="display:block; margin:auto;"/>
</p>

<p align="center">
  <img src="https://github.com/Bohdan-Somriakov/Evolution_of_Aggression/blob/main/examples/example12/population_simulation_hist.png" alt="Image" style="display:block; margin:auto;"/>
</p>

<p align="center">
  <img src="https://github.com/Bohdan-Somriakov/Evolution_of_Aggression/blob/main/examples/example12/population_simulation_pie.png" alt="Image" style="display:block; margin:auto; width:400px;"/>
</p>

<p align="center">
  <img src="https://github.com/Bohdan-Somriakov/Evolution_of_Aggression/blob/main/examples/example12/population_simulation_pies.png" alt="Image" style="display:block; margin:auto;"/>
</p>

The results are very stable

# Colclusion
Different rules and strategies have a profound impact on the outcomes for species. The conditions of the habitat, as well as the internal dynamics and rules governing each species, play crucial roles in determining their survival and population levels. For example, the availability of food, the behavior of Hawks and Doves, and their interactions with each other can drastically alter the balance within the ecosystem. The overall population is influenced by how these factors interplay, demonstrating the importance of both external environmental conditions and internal species strategies in shaping the ecosystem's dynamics.

## Plots

| Example 1 | Example 2 | Example 3 |
|-----------|-----------|-----------|
| ![Example 1](https://github.com/Bohdan-Somriakov/Evolution_of_Aggression/blob/main/examples/example1/population_simulation_graph.png) | ![Example 2](https://github.com/Bohdan-Somriakov/Evolution_of_Aggression/blob/main/examples/example2/population_simulation_graph.png) | ![Example 3](https://github.com/Bohdan-Somriakov/Evolution_of_Aggression/blob/main/examples/example3/population_simulation_graph.png) |

| Example 4 | Example 5 | Example 6 |
|-----------|-----------|-----------|
| ![Example 4](https://github.com/Bohdan-Somriakov/Evolution_of_Aggression/blob/main/examples/example4/population_simulation_graph.png) | ![Example 5](https://github.com/Bohdan-Somriakov/Evolution_of_Aggression/blob/main/examples/example5/population_simulation_graph.png) | ![Example 6](https://github.com/Bohdan-Somriakov/Evolution_of_Aggression/blob/main/examples/example6/population_simulation_graph.png) |

| Example 7 | Example 8 | Example 9 |
|-----------|-----------|-----------|
| ![Example 7](https://github.com/Bohdan-Somriakov/Evolution_of_Aggression/blob/main/examples/example7/population_simulation_graph.png) | ![Example 8](https://github.com/Bohdan-Somriakov/Evolution_of_Aggression/blob/main/examples/example8/population_simulation_graph.png) | ![Example 9](https://github.com/Bohdan-Somriakov/Evolution_of_Aggression/blob/main/examples/example9/population_simulation_graph.png) |

| Example 10 | Example 11 | Example 12 |
|------------|------------|------------|
| ![Example 10](https://github.com/Bohdan-Somriakov/Evolution_of_Aggression/blob/main/examples/example10/population_simulation_graph.png) | ![Example 11](https://github.com/Bohdan-Somriakov/Evolution_of_Aggression/blob/main/examples/example11/population_simulation_graph.png) | ![Example 12](https://github.com/Bohdan-Somriakov/Evolution_of_Aggression/blob/main/examples/example12/population_simulation_graph.png) |


## Pies

| Example 1 | Example 2 | Example 3 |
|-----------|-----------|-----------|
| ![Example 1](https://github.com/Bohdan-Somriakov/Evolution_of_Aggression/blob/main/examples/example1/population_simulation_pies.png) | ![Example 2](https://github.com/Bohdan-Somriakov/Evolution_of_Aggression/blob/main/examples/example2/population_simulation_pies.png) | ![Example 3](https://github.com/Bohdan-Somriakov/Evolution_of_Aggression/blob/main/examples/example3/population_simulation_pies.png) |

| Example 4 | Example 5 | Example 6 |
|-----------|-----------|-----------|
| ![Example 4](https://github.com/Bohdan-Somriakov/Evolution_of_Aggression/blob/main/examples/example4/population_simulation_pies.png) | ![Example 5](https://github.com/Bohdan-Somriakov/Evolution_of_Aggression/blob/main/examples/example5/population_simulation_pies.png) | ![Example 6](https://github.com/Bohdan-Somriakov/Evolution_of_Aggression/blob/main/examples/example6/population_simulation_pies.png) |

| Example 7 | Example 8 | Example 9 |
|-----------|-----------|-----------|
| ![Example 7](https://github.com/Bohdan-Somriakov/Evolution_of_Aggression/blob/main/examples/example7/population_simulation_pies.png) | ![Example 8](https://github.com/Bohdan-Somriakov/Evolution_of_Aggression/blob/main/examples/example8/population_simulation_pies.png) | ![Example 9](https://github.com/Bohdan-Somriakov/Evolution_of_Aggression/blob/main/examples/example9/population_simulation_pies.png) |

| Example 10 | Example 11 | Example 12 |
|------------|------------|------------|
| ![Example 10](https://github.com/Bohdan-Somriakov/Evolution_of_Aggression/blob/main/examples/example10/population_simulation_pies.png) | ![Example 11](https://github.com/Bohdan-Somriakov/Evolution_of_Aggression/blob/main/examples/example11/population_simulation_pies.png) | ![Example 12](https://github.com/Bohdan-Somriakov/Evolution_of_Aggression/blob/main/examples/example12/population_simulation_pies.png) |


# Credit
Inspired by https://www.youtube.com/watch?v=YNMkADpvO4w
