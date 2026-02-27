def test_demo():
    assert 1 + 1 == 2
def test_demo_fail():
    assert 1 + 1 == 2

def test_demo_response():
    from python.demo import demo
    result = demo()
    assert result == "Success"