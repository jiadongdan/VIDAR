import pytest

class TestColor:

    def test_colors(self):
        try:
            from vidar.colors import cc
        except ModuleNotFoundError:
            pytest.fail("Not found: the module vidar.colors")

    def test_color_keys(self):
        from vidar.colors import cc

        with pytest.raises(KeyError):
            cc['jack_spiral']
            cc['none']
            cc['a_dog']
            cc['X_man']
        
        try:
            cc['tab10'] 
            cc['tab20'] 
            cc['vega20'] 
            cc['math97']
            cc['math98']
            cc['deep']
            cc['muted']
            cc['pastel']
            cc['bright'] 
            cc['dark'] 
            cc['colorblind'] 
            cc['simple']
        except KeyError:
            pytest.fail("Key missing: the module vidar.colors.cc")

