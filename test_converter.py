from converter import convert

def test_positive():
    assert convert(100,52.851)==5285.1
    assert convert(30,52.851)==1585.53

def test_float():
    assert convert(.5,52.851)==26.4255
    assert convert(10.5,52.851)==554.9355

def test_zero():
    assert convert(0,52.851)==0
    