import pytest


pytest_plugins = [
    "mypackage.plugin",
    "mypackage.plugin2",
    # "mypackage.plugin3",
]


def pytest_configure(config: pytest.Config) -> None:
    print(__name__, "Configured")
