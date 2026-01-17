from core.base_agent import BaseAgent

class CustomerIntentAgent(BaseAgent):
    def __init__(self):
        super().__init__("Intent-Agent")

    def detect_intent(self, text):
        self.log("Detecting intent (MOCK)")
        return "order_food"
