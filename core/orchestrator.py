from core.base_agent import BaseAgent
from core.state_machine import OrderState

class OrchestratorAgent(BaseAgent):
    def __init__(
        self,
        intent_agent,
        menu_agent,
        restaurant_agent,
        order_agent,
        payment_agent,
        delivery_agent,
        tracking_agent
    ):
        super().__init__("Orchestrator")
        self.intent_agent = intent_agent
        self.menu_agent = menu_agent
        self.restaurant_agent = restaurant_agent
        self.order_agent = order_agent
        self.payment_agent = payment_agent
        self.delivery_agent = delivery_agent
        self.tracking_agent = tracking_agent

    def run(self, user_input):
        try:
            intent = self.intent_agent.detect_intent(user_input)
            if intent != "order_food":
                raise Exception("Unsupported intent")

            items = self.menu_agent.extract_items(user_input)
            restaurant = self.restaurant_agent.find_restaurant(items)

            order = self.order_agent.create_order(items, restaurant)
            self.order_agent.transition(order, OrderState.PAYMENT_PENDING)

            payment = self.payment_agent.process_payment(order["order_id"], 350)
            if payment["status"] != "SUCCESS":
                raise Exception("Payment failed")

            self.order_agent.transition(order, OrderState.PAID)

            delivery = self.delivery_agent.assign(order["order_id"])
            order["delivery"] = delivery
            self.order_agent.transition(order, OrderState.OUT_FOR_DELIVERY)

            order["tracking"] = self.tracking_agent.track(order["order_id"])
            self.order_agent.transition(order, OrderState.DELIVERED)

            return order

        except Exception as e:
            self.log(str(e))
            order["state"] = OrderState.FAILED
            return order
