![Python versions: 3.4, 3.5, 3.6](https://img.shields.io/pypi/pyversions/Django.svg)
# Neural Snake

Train a Neural Network to play Snake using a Genetic Algorithm.

==============================

Getting Started
------------
To install required libraries: 

`$ pip install -r requierments.txt`

To run on Windows you will have to additionally install curses:

`pip install windows-curses`

Running project
------------

`$ cd SnakeAi`

or

`$ cd ImprovedSnakeAI`

Run game with existing bot:

`$ python main.py <path-to-genome>`

Run genetic algorithm to create new bots:

`$ python ai.py`


Project Organization
------------

    ├── README.md                 <- Information about the project.
    ├── requiermnts.txt           <- File for installation of additional libraries.
    ├── SnakeAI                   <- First version of project
    │   ├── main.py               <- Run genetic algorithm to create new bots
    │   ├── ai.py                 <- The final, ca
    │   ├── game.py               <- Implementation of game and related API
    │   ├── config-feedforward    <- GA config file
    │   └── bots                  <- Folder with some pre-created bots
    ├── ImprovedSnakeAI           <- Second version of project
    │   ├── main.py               <- Run genetic algorithm to create new bots
    │   ├── ai.py                 <- The final, ca
    │   ├── game.py               <- Implementation of game and related API
    │   ├── config-feedforward    <- GA config file
    │   ├── visualize.py          <- Visualiztion of neural network architecture
    │   └── bots                  <- Folder with some pre-created bots
--------
