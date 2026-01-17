from core.base_agent import BaseAgent

class MenuUnderstandingAgent(BaseAgent):
    def __init__(self):
        super().__init__("Menu-Agent")

    def extract_items(self, text):
        self.log("Extracting items (MOCK)")
        return [
            {"name": "Chicken Biryani", "qty": 1},
            {"name": "Coke", "qty": 1}
        ]
