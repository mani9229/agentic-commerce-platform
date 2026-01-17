import sys
import os
sys.path.append(os.path.dirname(os.path.dirname(os.path.abspath(__file__))))

from agents.intent_agent import CustomerIntentAgent
from agents.menu_agent import MenuUnderstandingAgent
from agents.restaurant_agent import RestaurantDiscoveryAgent
from agents.order_agent import OrderManagementAgent
from agents.payment_agent import PaymentAgent
from agents.delivery_agent import DeliveryAssignmentAgent
from agents.tracking_agent import TrackingAgent
from core.orchestrator import OrchestratorAgent


orchestrator = OrchestratorAgent(
    CustomerIntentAgent(),
    MenuUnderstandingAgent(),
    RestaurantDiscoveryAgent(),
    OrderManagementAgent(),
    PaymentAgent(),
    DeliveryAssignmentAgent(),
    TrackingAgent()
)

result = orchestrator.run("Order Mutton biryani with butter chicken and icecream")
print(result)
