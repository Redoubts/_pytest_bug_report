import pytest


class Something:
    @pytest.hookimpl(trylast=True)  # this causes the issue
    def pytest_configure(self, config: pytest.Config) -> None:
        print(__name__, "Configured")
