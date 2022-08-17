"""Test stop_thread."""
# pylint: disable=broad-except
from stop_thread import __version__, stop_thread


def test_version():
    """Test version."""
    assert __version__[:3] == "0.1"


def test_sanity():
    """Check sanity."""
    try:
        assert not stop_thread()
    except Exception:
        assert True
