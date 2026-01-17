from core.base_agent import BaseAgent

class TrackingAgent(BaseAgent):
    def __init__(self):
        super().__init__("Tracking-Agent")

    def track(self, order_id):
        self.log("Tracking order (MOCK)")
        return [
            {"status": "PICKED"},
            {"status": "ON_THE_WAY"},
            {"status": "DELIVERED"}
        ]
