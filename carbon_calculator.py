# carbon_calculator.py

TRANSPORT_EMISSIONS = {
    "car": 0.21,
    "bike": 0.09,
    "bus": 0.05,
    "train": 0.04,
    "walk": 0
}


def calculate_carbon(transport, distance, electricity, diet):
    transport = transport.lower()
    diet = diet.lower()

    transport_co2 = TRANSPORT_EMISSIONS.get(transport, 0) * distance

    electricity_co2 = electricity * 0.4

    diet_co2 = 30 if diet == "nonveg" else 10

    total_co2 = transport_co2 + electricity_co2 + diet_co2

    return round(total_co2, 2)