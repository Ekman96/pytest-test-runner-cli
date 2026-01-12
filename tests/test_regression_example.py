import pytest

@pytest.mark.regression
def test_regression_example():
    assert "qa".upper() == "QA"
