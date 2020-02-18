from game import run_game
import neat
import os
import pickle

if __name__ == '__main__':
	local_dir = os.path.dirname(__file__)
	genome_path = os.path.join(local_dir, 'winner_genome')
	config_path = os.path.join(local_dir, 'config-feedforward')
	config = neat.Config(neat.DefaultGenome, neat.DefaultReproduction,
								neat.DefaultSpeciesSet, neat.DefaultStagnation,
								config_path)
	with open(genome_path, 'rb') as f:
		winner = pickle.load(f)
	winner_net = neat.nn.FeedForwardNetwork.create(winner, config)
	run_game(winner_net, 1, gui=True)
