class Televison:

    MUTE_VOLUME: int = 0
    MIN_VOLUME: int = 0
    MAX_VOLUME: int = 2
    MIN_CHANNEL: int = 0
    MAX_CHANNEL: int = 3

    def __init__(self):
        self.__status : bool = False
        self.__muted : bool = False
        self.__volume: int = Televison.MIN_VOLUME
        self.__channel: int = Televison.MIN_CHANNEL
        self.__prev_volume: int = Televison.MIN_VOLUME

    def power(self):
        """
        Turns the TV status to true or false
        :return: nothing
        """
        self.__status = not self.__status



    def mute(self):
        """
        Makes the volume of the TV zero
        :return: nothing
        """
        if self.__status:
            if not self.__muted:
                self.__prev_volume = self.__volume
                self.__volume = 0
                self.__muted = True
            else:
                self.__volume = self.__prev_volume
                self.__muted = False


    def channel_up(self):
        """
        Makes the channel go one up
        :return: nothing
        """
        if self.__status:
            if self.__channel < Televison.MAX_CHANNEL:
                self.__channel += 1
            else:
                self.__channel = Televison.MIN_CHANNEL
        else:
            pass
    def channel_down(self):
        """
        Makes the channel go one down
        :return: nothing
        """
        if self.__status:
            if self.__channel == Televison.MIN_CHANNEL:
                self.__channel = Televison.MAX_CHANNEL
            else:
                self.__channel -= 1
        else:
            pass

    def volume_up(self):
        """
        Makes the volume go one up
        :return: nothing
        """
        if self.__status:
            if self.__muted:
                self.__volume = self.__prev_volume
                self.__muted = False

            if self.__volume < Televison.MAX_VOLUME:
                self.__volume += 1

    def volume_down(self):
        """
        Makes the volume go one down
        :return: nothing
        """
        if self.__status:
            if self.__muted:
                self.__volume = self.__prev_volume
                self.__muted = False

            if self.__volume > Televison.MIN_VOLUME:
                self.__volume -= 1

    def __str__(self):
        """
        Returns the power, channel, and volume status of the TV

        """
        return(f"Power - [{self.__status}], Channel - [{self.__channel}], Volume - [{self.__volume}]")









