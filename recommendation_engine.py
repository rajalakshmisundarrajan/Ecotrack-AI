# recommendation_engine.py

def generate_recommendations(carbon_score):
    if carbon_score > 150:
        eco_score = 30
        category = "High Emissions 🔴"

        recommendations = [
            "Use public transport more often.",
            "Switch to LED bulbs.",
            "Reduce meat consumption.",
            "Turn off unused appliances."
        ]

    elif carbon_score > 80:
        eco_score = 60
        category = "Moderate Emissions 🟡"

        recommendations = [
            "Walk or cycle for short distances.",
            "Save electricity whenever possible.",
            "Avoid single-use plastics."
        ]

    else:
        eco_score = 90
        category = "Eco-Friendly 🟢"

        recommendations = [
            "Great job! Continue your sustainable habits.",
            "Encourage others to go green."
        ]

    return eco_score, category, recommendations
