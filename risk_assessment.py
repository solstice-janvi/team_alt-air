import random

class routeRiskAssessmentAI:
    def __init__(self):
        self.weather_conditions = ["Clear", "Rainy", "Snowy", "Foggy", "Stormy"]
        self.terrain_difficulty = ["Easy", "Moderate", "Difficult"]
        self.equipment_quality = ["Good", "Average", "Poor"]

    def assess_risk(self, weather, terrain, equipment):
        # Simulate a simple risk assessment based on random factors
        weather_index = self.weather_conditions.index(weather)
        terrain_index = self.terrain_difficulty.index(terrain)
        equipment_index = self.equipment_quality.index(equipment)

        risk_score = weather_index + terrain_index + equipment_index
        return risk_score

    def suggest_action(self, risk_score):
        if risk_score <= 3:
            return "Low risk. go safely."
        elif risk_score <= 6:
            return "Moderate risk. Be cautious and prepared."
        else:
            return "High risk. Consider path carefully."

if __name__ == "__main__":
    risk_assessment_ai = routeRiskAssessmentAI()

    # Simulate user inputs (you can replace these with actual data)
    weather_condition = random.choice(risk_assessment_ai.weather_conditions)
    terrain_difficulty = random.choice(risk_assessment_ai.terrain_difficulty)
    equipment_quality = random.choice(risk_assessment_ai.equipment_quality)

    print(f"Weather Condition: {weather_condition}")
    print(f"Terrain Difficulty: {terrain_difficulty}")
    print(f"Equipment Quality: {equipment_quality}")

    risk_score = risk_assessment_ai.assess_risk(weather_condition, terrain_difficulty, equipment_quality)
    suggested_action = risk_assessment_ai.suggest_action(risk_score)

    print(f"Risk Score: {risk_score}")
    print(f"Suggested Action: {suggested_action}")
