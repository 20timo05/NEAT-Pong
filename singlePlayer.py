import pickle
from multiPlayer import startGame

from train import trainAI, save_neural_network

def load_neural_network(file_path):
    try:
        with open(file_path, 'rb') as file:
            nn = pickle.load(file)
        return nn
    except FileNotFoundError:
        # Handle the case when the file does not exist
        print(f"File '{file_path}' not found. Creating a new neural network.")
        # Create and return a new neural network object here
        nn = trainAI()
        save_neural_network(nn, file_path)
        return nn
    
if __name__ == "__main__":
    nn = load_neural_network("PONG_NN.pkl")
    startGame(opponentGenome = nn, showOpponentInput = True)
