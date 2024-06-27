import pytest

class TestVIDAR:

    def test_components(self):
        try:
            import vidar.clustering
            import vidar.colors
            import vidar.interactive
        except ModuleNotFoundError:
            pytest.fail("Not found: the module vidar.colors")
