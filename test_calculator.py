from carbon_calculator import calculate_carbon


def test_carbon_calculation():
    result = calculate_carbon(
        "car",
        20,
        100,
        "veg"
    )

    assert result > 0