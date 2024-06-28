import pytest
import numpy as np

class TestInteractiveKMeans:

    def test_module(self):
        try:
            from vidar import InteractiveKMeans, interactive_kmeans
        except ModuleNotFoundError:
            pytest.fail("Not found: InteractiveKMeans, interactive_kmeans")

    def test_function_call(self):
        from vidar import interactive_kmeans

        X = np.random.random((10,2))
        with pytest.raises(AttributeError):
            app = interactive_kmeans(X)
            app.xx()
            
        try:
            app = interactive_kmeans(X)
            app.update_cluster()
            app.plot_figure()
        except AttributeError:
            pytest.fail(
                "Function missing: the function missing in the class InteractiveKMeans"
                )

    