# Testing repeatafterme.py
import pytest
from repeatafterme import Sound, SoundList, Player, Game, Display

@pytest.fixture
def sound_list() -> None:
    sl = SoundList()

    return sl

def test_SoundList_classV1(sound_list: SoundList) -> None:
    sound = Sound("Repeat-After-Me/sounds/soundA", 'A')
    try:
        sound_list.append(12)

    except TypeError:
        assert True

def test_SoundList_classV2(sound_list: SoundList) -> None:
    sound = Sound("Repeat-After-Me/sounds/soundA", 'A')
    sound_list.append(sound)

    assert isinstance(sound_list[-1], Sound)

def test_Display_class() -> None:
    d = Display
    player = d.display_rules(d)

    assert isinstance(player, Player)
    assert isinstance(player.player_name, str)


# testing methods of Game class
def test_appender_method(sound_list: SoundList) -> None:
    sl = sound_list
    sound_A = Sound(sound_path="Repeat-After-Me/sounds/soundA.wav", sound_name='A')
    sound_S = Sound(sound_path="Repeat-After-Me/sounds/soundS.wav", sound_name='S')
    sound_D = Sound(sound_path="Repeat-After-Me/sounds/soundD.wav", sound_name='D')
    sound_F = Sound(sound_path="Repeat-After-Me/sounds/soundF.wav", sound_name='F')

    sounds = [sound_A, sound_S, sound_D, sound_F]
    g = Game
    pattern = ""
    p = g.appender(g, sl, sounds, pattern)

    assert len(sound_list) != 0
    assert isinstance(p, str)
    assert p[-1] == sound_list[-1].sound_name

