from Board import Board
from Cell import *
from utils import *

class Card(object):

    def __int__(self,rotation, xcoordinate, ycoordinate):
        self.rotation = rotation
        self.first_cell = Cell(rotation[1] ,rotation[2],xcoordinate,ycoordinate)
        self.second_cell = get_second_cell(rotation, xcoordinate, ycoordinate)

    def get_first_cell(self):
        return self.first_cell

    def get_second_cell(self):
        return self.second_cell

