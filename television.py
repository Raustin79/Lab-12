


class Television:
    """Class to represent a television functions"""

    MIN_VOLUME: int = 0
    MAX_VOLUME: int = 2
    MIN_CHANNEL: int = 0
    MAX_CHANNEL: int = 3

    def __init__(self) -> None:
        """Set values for television functions"""

        self.__status: bool = False
        self.__muted: bool = False
        self.__volume: int = Television.MIN_VOLUME
        self.__channel: int = Television.MIN_CHANNEL

    def power(self) -> None:
        """Power the television functions"""
        self.__status = not self.__status

    def mute(self) -> None:
        """Mute the television functions"""
        if self.__status:
            self.__muted = not self.__muted


    def channel_up(self) -> None:
        """Increase the television functions channel up"""
        if self.__status:
            if self.__channel >= Television.MAX_CHANNEL:
                self.__channel = Television.MIN_CHANNEL
            else:
                self.__channel += 1

    def channel_down(self) -> None:
        """Decrease the television functions channel down"""
        if self.__status:
            if self.__channel <= Television.MIN_CHANNEL:
                self.__channel = Television.MAX_CHANNEL
            else:
                self.__channel -= 1

    def volume_up(self) -> None:
        """Increase the volume by one"""
        if self.__status:
            self.__muted = False
            if self.__volume < Television.MAX_VOLUME:
                self.__volume += 1

    def volume_down(self) -> None:
        """Decrease the volume by one"""
        if self.__status:
            self.__muted = False
            if self.__volume > Television.MIN_VOLUME:
                self.__volume -= 1

    def __str__(self) -> str:
        """Return a string representation of the television functions"""
        if self.__muted:
            volume: int = Television.MIN_VOLUME
        else:
            volume: int = self.__volume

        return f'Power = {self.__status}, 'f'Channel = {self.__channel}, 'f'Volume = {volume}'









