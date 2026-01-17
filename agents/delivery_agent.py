from core.base_agent import BaseAgent

class DeliveryAssignmentAgent(BaseAgent):
    def __init__(self):
        super().__init__("Delivery-Agent")

    def assign(self, order_id):
        self.log("Assigning delivery partner")
        return {"partner": "Ravi", "vehicle": "Bike"}
