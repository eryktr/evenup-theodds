import pytest
from evenuptheodds.configparser import ConfigParser
from evenuptheodds.errors import NoConfigFileError

def test_configparser_raises_when_configfile_doesnt_exist(monkeypatch):
    parser = ConfigParser()
    monkeypatch.setattr(parser, "_CONFIGFILE", "i/do/not/exist")
    
    with pytest.raises(NoConfigFileError):
        parser.parse()


def test_configparser_parses_players_correctly():
    parser = ConfigParser()
    parser.parse()