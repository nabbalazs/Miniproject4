import tkinter as tk
import time
import random
import pytest

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

def test_stop_timer(gui):
    gui.start_timer()
    gui.stop_timer()
    assert not gui.is_running

def test_leaderboard_update(gui):
    initial_leaderboard = gui.load_leaderboard()
    gui.start_timer()
    time.sleep(2)
    gui.stop_timer()
    updated_leaderboard = gui.load_leaderboard()
    assert updated_leaderboard != initial_leaderboard

def test_restart_timer(gui):
    gui.start_timer()
    gui.restart_timer()
    assert not gui.is_running
    assert gui.elapsed_time == 0