import pytest
from television import *

@pytest.fixture
def tv() -> Television:
    return Television()


def test_init(tv) -> None:
    assert str(tv) == 'Power = False, Channel = 0, Volume = 0'

def test_power(tv) -> None:
    tv.power()
    assert str(tv) =='Power = True, Channel = 0, Volume = 0'
    tv.power()
    assert str(tv) =='Power = False, Channel = 0, Volume = 0'

def test_mute(tv) -> None:
    tv.power()
    tv.volume_up()
    tv.mute()
    assert str(tv) =='Power = True, Channel = 0, Volume = 0'

    #on and unmuted
    tv.mute()
    assert str(tv) =='Power = True, Channel = 0, Volume = 1'

    # off and muted
    tv.power()
    tv.mute()
    assert str(tv) =='Power = False, Channel = 0, Volume = 1'

    # off and unmuted
    tv.mute()
    assert str (tv) =='Power = False, Channel = 0, Volume = 1'

def test_channel_up(tv) -> None:
    # off and channel up
    tv.channel_up()
    assert str(tv) =='Power = False, Channel = 0, Volume = 0'

    # on and channel up
    tv.power()
    tv.channel_up()
    assert str(tv) =='Power = True, Channel = 1, Volume = 0'

    # on and pushed pass max
    tv.channel_up()
    tv.channel_up()
    tv.channel_up()
    assert str(tv) =='Power = True, Channel = 0, Volume = 0'

def test_channel_down(tv) -> None:
    # off and channel decreased
    tv.channel_down()
    assert str(tv) =='Power = False, Channel = 0, Volume = 0'

    #on and channel decreased pass min
    tv.power()
    tv.channel_down()
    assert str(tv) =='Power = True, Channel = 3, Volume = 0'

def test_volume_up(tv) -> None:
    # Off and volume increased
    tv.volume_up()
    assert str(tv) =='Power = False, Channel = 0, Volume = 0'

    # On and volume increased
    tv.power()
    tv.volume_up()
    assert str(tv) =='Power = True, Channel = 0, Volume = 1'

    # One, muted, and volume increased
    tv.mute()
    tv.volume_up()
    assert str(tv) =='Power = True, Channel = 0, Volume = 2'

    # On and volume increased pass max
    tv.volume_up()
    assert str (tv) =='Power = True, Channel = 0, Volume = 2'

def test_volume_down(tv) -> None:
    # Off and volume decreased
    tv.volume_down()
    assert str(tv) =='Power = False, Channel = 0, Volume = 0'

    # On and volume decreased (max first)
    tv.power()
    tv.volume_up()
    tv.volume_up()
    tv.volume_down()
    assert str(tv) =='Power = True, Channel = , Volume = 1'

    # On, muted and volume decreased
    tv.volume_up()
    tv.mute()
    tv.volume_down()
    assert str(tv) =='Power = True, Channel = 0, Volume = 1'

    # On and volume decreased past min
    tv.volume_down()
    tv.volume_down()
    assert str(tv) =='Power = True, Channel = 0, Volume = 0'























