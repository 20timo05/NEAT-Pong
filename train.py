import pickle
from NEAT.Neat import Neat
from PongGameWrapper import PongGameWrapper
from multiPlayer import startGame

def trainAI():
    neat = Neat(3, 3, 50)
    SHOW_GAME = False

    trained_opponent = None

    for generation in range(50):
      if generation > 40 and SHOW_GAME == False: SHOW_GAME = True
      # evaluate genomes
      # let all clients play against all other clients to calcalute a fair fitness score
      SCREEN_WIDTH = 800
      SCREEN_HEIGHT = 600

      for idx1, client1 in enumerate(neat.clients):
        if idx1 == len(neat.clients) + 1: break
        client1.score = 0
        for idx2, client2 in enumerate(neat.clients[idx1 + 1:]):
          client2.score = 0 if client2.score == None else client2.score
          game = PongGameWrapper(None, False, SCREEN_WIDTH, SCREEN_HEIGHT)
          game.trainAI(client1, client2, idx1, idx2)

          # sufficiently good agent found
          if client1.score > 300: trained_opponent = client1

      neat.evolve()
      neat.print_information()
      print(f"GENERATION {generation + 1}")

      if trained_opponent != None: break

    if trained_opponent == None:
      trained_opponent = max(neat.clients, key=lambda c: c.score)

    return trained_opponent

# save Genome
def save_neural_network(nn, file_path):
    with open(file_path, 'wb') as file:
        pickle.dump(nn, file)

if __name__ == "__main__":
    nn = trainAI()
    save_neural_network(nn, "PONG_NN.pkl")