import Lab2.bmi as bmi

def test_bmi_underweight():
    expected_result = -1
    result = bmi.calculate_bmi(1.73,40)
    assert (result == expected_result)

def test_bmi_normalweight():
    expected_result = 0
    result = bmi.calculate_bmi(1.73,70)
    assert (result == expected_result)

def test_bmi_overweight():
    expected_result = 1
    result = bmi.calculate_bmi(1.73,120)
    assert (result == expected_result)
