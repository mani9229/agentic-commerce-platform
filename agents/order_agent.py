from core.base_agent import BaseAgent
from core.state_machine import OrderState

class OrderManagementAgent(BaseAgent):
    def __init__(self):
        super().__init__("Order-Agent")
        self.order_id = 1000

    def create_order(self, items, restaurant):
        self.order_id += 1
        self.log("Creating order")
        return {
            "order_id": self.order_id,
            "items": items,
            "restaurant": restaurant,
            "state": OrderState.CREATED
        }

    def transition(self, order, new_state):
        self.log(f"Transition {order['state']} → {new_state}")
        order["state"] = new_state
