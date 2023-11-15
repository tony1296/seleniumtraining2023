def sum(a,b):
    return a+b

def test_calc_sum_1():
    result = sum(2,3)
    assert result == 5
    
def test_calc_sum_2():
    result = sum(3,3)
    assert result == 6

def test_calc_sum_3():
    result = sum(5,4)
    assert result == 9

def test_calc_sum_4():
    result = sum(5,3)
    assert result == 8

def test_calc_sum_5():
    result = sum(6,6)
    assert result == 12
