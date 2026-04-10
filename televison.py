class Televison:

    MUTE_VOLUME = 0
    MIN_VOLUME = 0
    MAX_VOLUME = 2
    MIN_CHANNEL = 0
    MAX_CHANNEL = 3

    def __init__(self):
        self.__status = False
        self.__muted = False
        self.__volume = Televison.MIN_VOLUME
        self.__channel = Televison.MIN_CHANNEL
        self.__prev_volume = Televison.MIN_VOLUME

    def power(self):
        self.__status = not self.__status



    def mute(self):
        if self.__status:
            if not self.__muted:
                self.__prev_volume = self.__volume
                self.__volume = 0
                self.__muted = True
            else:
                self.__volume = self.__prev_volume
                self.__muted = False


    def channel_up(self):
        if self.__status:
            if self.__channel < Televison.MAX_CHANNEL:
                self.__channel += 1
            else:
                self.__channel = Televison.MIN_CHANNEL
        else:
            pass
    def channel_down(self):
        if self.__status:
            if self.__channel == Televison.MIN_CHANNEL:
                self.__channel = Televison.MAX_CHANNEL
            else:
                self.__channel -= 1
        else:
            pass

    def volume_up(self):
        if self.__status:
            if self.__muted:
                self.__volume = self.__prev_volume
                self.__muted = False

            if self.__volume < Televison.MAX_VOLUME:
                self.__volume += 1

    def volume_down(self):
        if self.__status:
            if self.__muted:
                self.__volume = self.__prev_volume
                self.__muted = False

            if self.__volume > Televison.MIN_VOLUME:
                self.__volume -= 1
    def __str__(self):
        return(f"Power - [{self.__status}], Channel - [{self.__channel}], Volume - [{self.__volume}]")









