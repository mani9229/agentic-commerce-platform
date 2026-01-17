from core.base_agent import BaseAgent

class PaymentAgent(BaseAgent):
    def __init__(self):
        super().__init__("Payment-Agent")

    def process_payment(self, order_id, amount):
        self.log(f"Processing payment ₹{amount} (MOCK)")
        return {"status": "SUCCESS", "payment_id": f"MOCKPAY-{order_id}"}
