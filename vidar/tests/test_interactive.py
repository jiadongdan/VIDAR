import pytest
import numpy as np

class TestInteractive:

    def test_module(self):
        try:
            from vidar.interactive import interactive_layout
        except ModuleNotFoundError:
            pytest.fail("Not found: the module vidar.interactive.interactive_layout")

    def test_function_call(self):
        from vidar.interactive import interactive_layout

        with pytest.raises(AttributeError):
            interactive_layout.colors_from_sky()
            interactive_layout.colors_from_ss()
            
        try:
            value = interactive_layout.colors_from_lbs([1,2,3])
        except AttributeError:
            pytest.fail(
                "Key missing: the function colors_from_lbs in the module interactive_layout"
                )
        
        assert np.any(value == ['#ff7f0e', '#2ca02c', '#d62728'])
            
    def test_class(self):
        from vidar.interactive import interactive_layout

        try:
            import matplotlib.pyplot as plt
            import numpy as np
            pts = np.random.random((1000, 2))
            ps = np.random.random((1000, 45, 45))
            fig, ax = plt.subplots(1, 2, figsize=(12, 6))
            app = interactive_layout.InteractiveCluster(fig, pts, ps, lbs=None)
        except AttributeError:
            pytest.fail(
                "Class missing: the class InteractiveCluster in the module interactive_layout"
                )
        except TypeError:
            pytest.fail(
                "Parameter error: the class InteractiveCluster in the module interactive_layout"
                )
        

    