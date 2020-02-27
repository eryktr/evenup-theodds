import pytest
import pathlib

from evenuptheodds.configparser import ConfigParser
from evenuptheodds.errors import NoConfigFileError, InvalidPlayerDefinition, InvalidDivisionName, NameRepetition, \
    TooManyPlayers
from evenuptheodds.models import Player, Division


def test_configparser_raises_when_configfile_doesnt_exist(monkeypatch):
    parser = ConfigParser()
    monkeypatch.setattr(parser, "_CONFIGFILE", "i/do/not/exist")

    with pytest.raises(NoConfigFileError):
        parser.parse()


def test_configparser_raises_when_line_doesnt_match_player_regex(monkeypatch):
    def content():
        return """User1   Diamond IV
        iAmInvalid
        User2   Platinum IV"""

    monkeypatch.setattr(pathlib.Path, "read_text", lambda _: content())
    parser = ConfigParser()

    with pytest.raises(InvalidPlayerDefinition) as err:
        parser.parse()

    assert "iAmInvalid" == err.value.line.strip()


def test_configparser_raises_on_invalid_division(monkeypatch):
    def content():
        return """User1   Diamond IV
        User2   Silver VI
        User3   Plat IV"""

    monkeypatch.setattr(pathlib.Path, "read_text", lambda _: content())
    parser = ConfigParser()

    with pytest.raises(InvalidDivisionName) as err:
        parser.parse()

    assert "Silver VI" == err.value.divname


def test_configparser_raises_on_redeclared_player(monkeypatch):
    def content():
        return """User1   Diamond IV
        User1   Iron IV
        User3   Plat IV"""

    monkeypatch.setattr(pathlib.Path, "read_text", lambda _: content())
    parser = ConfigParser()

    with pytest.raises(NameRepetition) as err:
        parser.parse()

    assert "User1" == err.value.name


def test_configparser_raises_when_there_are_too_many_players(monkeypatch):
    def content():
        return "\n".join([f"User{i} SilverIV" for i in range(11)])

    monkeypatch.setattr(pathlib.Path, "read_text", lambda _: content())
    parser = ConfigParser()

    with pytest.raises(TooManyPlayers):
        parser.parse()


def test_configparser_parses_players_correctly(monkeypatch):
    def valid_config_file():
        return """User1   Diamond IV
        User2   Silver III
        User3   Challenger
        No1     Master"""

    monkeypatch.setattr(pathlib.Path, "read_text", lambda _: valid_config_file())
    parser = ConfigParser()
    users = parser.parse()
    assert [Player("User1", Division.D4), Player("User2", Division.S3), Player("User3", Division.C),
            Player("No1", Division.M)] == users
