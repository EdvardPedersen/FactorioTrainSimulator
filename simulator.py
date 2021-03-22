import pygame
from train import Train
from station import Station

class Simulation:
    def __init__(self):
        self.trains = []
        self.stations = []
        self.connections = []

    def add_train(self):
        self.trains.append(Train())

    def add_station(self):
        self.stations.append(Station())

    def update(self):


if __name__ == "__main__":
    s = Simulation()
    s.add_train()

