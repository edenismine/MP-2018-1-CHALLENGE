class Clock(object):
    def __init__ (self, h, m):
        self.__minutes = (h * 60 + m) % 1440

    def add(self, minutes):
        self.__minutes = (self.__minutes + minutes) % 1440
        return self

    def __repr__(self):
        t = [str(e) for e in divmod(self.__minutes, 60)]
        return ('00' if t[0] is '24' else t[0]).zfill(2) + ':' + t[1].zfill(2)

    def __eq__(self, other):
        return repr(self) == repr(other)
