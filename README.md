# Rectangle Overlap Project

## Project Overview

This project focuses on generating random stripes (rectangles) and running different algorithms to solve the rectangle overlap problem. The algorithms used in this project include:

1. Brute-force
2. Genetic Algorithms
3. Random Search
4. Greedy Algorithm

Additionally, experiments will be conducted to evaluate the performance of these algorithms based on various parameters such as the number of iterations and the number of stripes. The experiments aim to measure both the speed and precision of each algorithm.

## Project Structure

- **src/**
  - **main.py**: The main script to run the project.
  - **rectangle_generator.py**: Script to generate random rectangles.
  - **brute_force.py**: Implementation of the brute-force algorithm.
  - **genetic_algorithm.py**: Implementation of the genetic algorithm.
  - **random_search.py**: Implementation of the random search algorithm.
  - **greedy_algorithm.py**: Implementation of the greedy algorithm.
  - **experiments.py**: Scripts to run various experiments.

- **data/**
  - **rectangles.txt**: Example file containing rectangle coordinates.

- **results/**
  - Directory to store the results of experiments.

- **README.md**: Project overview and instructions.

## Requirements

- Python 3.x
- Required Python packages (can be installed via `requirements.txt`)

## Installation

1. Clone the repository:
    ```
    git clone https://github.com/khmelevskyi/rectangles-intersection-problem.git
    ```
2. Navigate to the project directory:
    ```
    cd rectangles-intersection-problem
    ```
3. Setup virtual environment and activate it
    ```
    python -m venv .venv
    source .venv/bin/activate
    ```
3. Install the required packages:
    ```
    pip install -r requirements.txt
    ```

## Usage

### Generate Random Rectangles

To start the main menu do:

```
python -m src.main
```


## Experiments

### Genetic Algorithm Experiments

Experiments with genetic algorithms will vary the maximum number of iterations to observe the impact on performance and accuracy.

### Random Search Experiments

Experiments with random search will vary the number of iterations for generating random solution vectors (X vectors) to observe the impact on performance and accuracy.

### Comparison Experiments

Experiments comparing all algorithms will be conducted to measure:

1. **Speed**: How fast each algorithm can solve the problem.
2. **Precision**: How accurate each algorithm is in solving the problem.

These experiments will vary the number of stripes to observe how the algorithms scale with problem size.

## Results

The results of the experiments will be stored in the `results/` directory. Each experiment will generate a report detailing the performance and accuracy of the algorithms under different conditions.

## License

This project is licensed under the MIT License.