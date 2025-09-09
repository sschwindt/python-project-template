from src.hydraulics.culvert import headwater_inlet_orifice, headwater_inlet_weir

def test_orifice_head_decreases_with_area():
    h_small = headwater_inlet_orifice(Q=1.0, A=0.2)
    h_large = headwater_inlet_orifice(Q=1.0, A=0.4)
    assert h_large < h_small

def test_weir_head_increases_with_Q():
    h1 = headwater_inlet_weir(Q=0.5, b=1.0)
    h2 = headwater_inlet_weir(Q=1.0, b=1.0)
    assert h2 > h1
