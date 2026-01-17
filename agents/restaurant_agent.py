from core.base_agent import BaseAgent

class RestaurantDiscoveryAgent(BaseAgent):
    def __init__(self):
        super().__init__("Restaurant-Agent")

    def find_restaurant(self, items):
        self.log("Finding restaurant (MOCK)")
        return {"id": 1, "name": "Mock Paradise Hotel", "eta": 30}
