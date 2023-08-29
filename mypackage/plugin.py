import pytest


@pytest.hookimpl(trylast=True)
def pytest_configure(config: pytest.Config) -> None:
    print(__name__, "Configured")
