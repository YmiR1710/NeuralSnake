from __future__ import print_function
import os
import neat
from game import run_game
import pickle


def eval_genomes(genomes, config):
    for genome_id, genome in genomes:
        genome.fitness = 0
        net = neat.nn.FeedForwardNetwork.create(genome, config)
        genome.fitness = run_game(net, 10, 0, gui=True)


def run(config_file):
    config = neat.Config(neat.DefaultGenome, neat.DefaultReproduction,
                         neat.DefaultSpeciesSet, neat.DefaultStagnation,
                         config_file)
    p = neat.Population(config)
    p.add_reporter(neat.StdOutReporter(True))
    p.add_reporter(neat.StatisticsReporter())
    p.add_reporter(neat.Checkpointer(5))
    winner = p.run(eval_genomes, 200)
    print('\nBest genome:\n{!s}'.format(winner))
    with open('winner_genome', 'wb') as f:
        pickle.dump(winner, f)
    winner_net = neat.nn.FeedForwardNetwork.create(winner, config)



if __name__ == '__main__':
    local_dir = os.path.dirname(__file__)
    config_path = os.path.join(local_dir, 'config-feedforward')
    run(config_path)
