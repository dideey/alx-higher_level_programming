#!/usr/bin/python3

"""class square"""

from models.rectangle import Rectangle

class Square(Rectangle):
    """"""

    def __init__(self, size, x=0, y=0, id=None):

        super().__init__(size, size, id, x, y)
        self.__width = size
        self.__height = size

    @property
    def size(self):
        return self.width

    @size.setter
    def size(self, value):
        self.width = value
        self.height = value
        

    def __str__(self):
        
        iid = "({})".format(self.id)
        xy = " {}/{} - ".format(self.x, self.y)
        size = "{}".format(self.height)

        return "[Square]" + iid + xy + size

    def update(self, *args, **kwargs):

        if args:
            attributes = ["id", "size", "x", "y"]
            for i, value in enumerate(args):
                setattr(self, attributes[i], value)

        if kwargs:
            for key, value in kwargs.items():
                setattr(self, key, value)

    def to_dictionary(self):
        return {
                'id' : self.id,
                'size' : self.size,
                'x' : self.x,
                'y' : self.y,
                }
