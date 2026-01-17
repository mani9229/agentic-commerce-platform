import sys
import os
sys.path.append(os.path.dirname(os.path.dirname(os.path.abspath(__file__))))

from fastapi import FastAPI
from pydantic import BaseModel

from agents.intent_agent import CustomerIntentAgent
from agents.menu_agent import MenuUnderstandingAgent
from agents.restaurant_agent import RestaurantDiscoveryAgent
from agents.order_agent import OrderManagementAgent
from agents.payment_agent import PaymentAgent
from agents.delivery_agent import DeliveryAssignmentAgent
from agents.tracking_agent import TrackingAgent
from core.orchestrator import OrchestratorAgent

app = FastAPI(title="Agentic Commerce Platform")

# Instantiate agents once (platform-style)
orchestrator = OrchestratorAgent(
    CustomerIntentAgent(),
    MenuUnderstandingAgent(),
    RestaurantDiscoveryAgent(),
    OrderManagementAgent(),
    PaymentAgent(),
    DeliveryAssignmentAgent(),
    TrackingAgent()
)

class OrderRequest(BaseModel):
    text: str

@app.post("/order")
def place_order(request: OrderRequest):
    result = orchestrator.run(request.text)
    return result
