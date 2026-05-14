import employee_info as EMPLOY


def test_calc_avg():
    expected_result = 60166.67
    result = EMPLOY.calculate_average_salary()
    assert (round(result,2) == expected_result)

def test_get_employee_by_dept():
    expected_result = [ EMPLOY.employee_data[1], EMPLOY.employee_data[2] ]
    result = EMPLOY.get_employees_by_dept("Marketing")
    assert (result == expected_result)

def test_get_by_range():
    expected_result = [ EMPLOY.employee_data[0], EMPLOY.employee_data[3], EMPLOY.employee_data[4]]
    result = EMPLOY.get_employees_by_age_range(29,36)
    assert (result == expected_result)
