import sys
import os
import pytest
import numpy as np

my_path = os.path.dirname(os.path.abspath(__file__))
sys.path.insert(0, my_path + '/../../')
from sindy.differentiation import differentiation_methods

# Note: all tests should be encapsulated in functions whose
# names start with "test_"

# To run tests, navigate to this directory in the terminal
# and run the command
# python3 -m pytest

# (normally you should just be able to run 'pytest' but
# there's something fishy going on with the imports)

# Simplest example: just use an assert statement
# This example should be removed eventually so that
# differentiators don't need to keep the endpoints
def test_forward_difference_length():
    x = 2 * np.linspace(1, 100, 100)
    assert len(differentiation_methods.forward_difference(x)) == len(x)


# Fixtures: data sets to be re-used in multiple tests
@pytest.fixture
def data_1d_linear():
    x = 2 * np.linspace(1, 100, 100).reshape(-1, 1)
    x_dot = 2 * np.ones(100).reshape(-1, 1)
    return x, x_dot


@pytest.fixture
def data_2d_linear():
    x = np.zeros((100, 2))
    x[:, 0] = 2 * np.linspace(1, 100, 100)
    x[:, 1] = -10 * np.linspace(1, 100, 100)

    x_dot = np.ones((100, 2))
    x_dot[:, 0] *= 2
    x_dot[:, 1] *= -10
    return x, x_dot


def test_forward_difference_1d(data_1d_linear):
    x, x_dot = data_1d_linear
    np.testing.assert_allclose(
        differentiation_methods.forward_difference(x),
        x_dot
    )


def test_forward_difference_2d(data_2d_linear):
    x, x_dot = data_2d_linear
    np.testing.assert_allclose(
        differentiation_methods.forward_difference(x),
        x_dot
    )


def test_centered_difference_1d(data_1d_linear):
    x, x_dot = data_1d_linear
    np.testing.assert_allclose(
        differentiation_methods.centered_difference(x),
        x_dot
    )


def test_centered_difference_2d(data_2d_linear):
    x, x_dot = data_2d_linear
    np.testing.assert_allclose(
        differentiation_methods.centered_difference(x),
        x_dot
    )


# Alternative implementation of the four tests above using parametrization
@pytest.mark.parametrize(
    'data',
    [
        (data_1d_linear()),
        (data_2d_linear())
    ]
)
def test_forward_difference(data):
    x, x_dot = data
    np.testing.assert_allclose(
        differentiation_methods.forward_difference(x),
        x_dot
    )

@pytest.mark.parametrize(
    'data',
    [
        (data_1d_linear()),
        (data_2d_linear())
    ]
)
def test_centered_difference(data):
    x, x_dot = data
    np.testing.assert_allclose(
        differentiation_methods.centered_difference(x),
        x_dot
    )


# pytest can also check that methods throw errors when appropriate
def test_forward_difference_dim():
    x = np.ones((5,5,5))
    with pytest.raises(ValueError):
        differentiation_methods.forward_difference(x)

def test_forward_difference_dim():
    x = np.ones((5,5,5))
    with pytest.raises(ValueError):
        differentiation_methods.centered_difference(x)