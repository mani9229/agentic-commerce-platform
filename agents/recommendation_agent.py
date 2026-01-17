from core.base_agent import BaseAgent

class RecommendationAgent(BaseAgent):
    def __init__(self):
        super().__init__("Recommendation-Agent")

    def recommend(self, user_id):
        self.log("Generating recommendations (MOCK)")
        return ["Butter Naan", "Gulab Jamun"]
