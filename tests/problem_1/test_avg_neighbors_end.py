import pytest
import numpy as np
from numpy.testing import assert_almost_equal

from ..tst import get_attribute, dzb64b16


FILENAME = "exercise.py"

@pytest.fixture(scope="module")
def avg_neighbors():
    return get_attribute("avg_neighbors", FILENAME)

exec(dzb64b16(b'789C35CBDF0A40301805F07B4F712EFD0FE162B527594BE45B89D04C6D9EDE907379CEEF8CA4A0429B628858001F078E75CF2FD2DBD12DD34CCF381AB713F7B55AB6DEB475F45151B2AC94FE50E40D628456B0AC92486045C5E48F8A4738F1C9E12D359953AF70C10DD30821F0'))

@pytest.mark.parametrize('b', [
    np.arange(11),
    np.arange(0, 100, 2.5),
    np.linspace(-1, 2, 10),
    np.arange(-20, 20, 4)])
def test_avg_neighbors_end(avg_neighbors, b, q=42.24):
    ref = f(b, q)
    value = avg_neighbors(b, end=q)
    assert_almost_equal(value, ref)

