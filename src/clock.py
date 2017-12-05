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

    def mirrored(self):
        hour, minute = tuple(map(int,self.__repr__().split(':')))
        hour = abs(12-(hour % 12))
        minute = abs((60-minute) % 60)
        return Clock(hour,minute)

if __name__ == '__main__':
    h, m = tuple(map(int, input("Enter the time using the following "
                                "format> hh:mm\n").strip().split(':')))
    c = Clock(h,m)
    print(c.mirrored())