import pytest
import tkinter as tk
from Timer import GUI

@pytest.fixture
def gui():
    root = tk.Tk()
    gui = GUI(root)
    yield gui
    root.destroy()

def test_start_timer(gui):
    gui.start_timer()
    assert gui.is_running
    assert gui.start_time != 0

def test_stop_timer(gui):
    gui.start_timer()
    gui.stop_timer()
    assert not gui.is_running
    assert gui.is_over

def test_restart_timer(gui):
    gui.start_timer()
    gui.stop_timer()
    gui.restart_timer()
    assert not gui.is_over
    assert gui.start_time == 0
    assert gui.elapsed_time == 0

def test_load_leaderboard(gui):
    leaderboard = gui.load_leaderboard()
    assert isinstance(leaderboard, str)
    assert "1." in leaderboard
    assert "2." in leaderboard
    assert "3." in leaderboard

def test_update_leaderboard(gui):
    initial_leaderboard = gui.load_leaderboard()
    gui.update_leaderboard("10.123")
    updated_leaderboard = gui.load_leaderboard()
    assert initial_leaderboard != updated_leaderboard

