from core.base_agent import BaseAgent

class MenuUnderstandingAgent(BaseAgent):
    def __init__(self):
        super().__init__("Menu-Agent")

        # Simple mock menu vocabulary
        self.menu_items = {
            "chicken biryani": "Chicken Biryani",
            "mutton biryani": "Mutton Biryani",
            "butter chicken": "Butter Chicken",
            "ice cream": "Ice Cream",
            "coke": "Coke"
        }

    def extract_items(self, text):
        self.log("Extracting items (SMART MOCK)")
        text = text.lower()

        items = []
        for key, value in self.menu_items.items():
            if key in text:
                items.append({"name": value, "qty": 1})

        # Fallback
        if not items:
            items.append({"name": "Chef Special", "qty": 1})

        return items
