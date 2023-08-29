import pytest


def pytest_configure(config: pytest.Config) -> None:
    print(__name__, "Configured")
    from .plugin3 import Something

    config.pluginmanager.register(Something())
