from core.base_agent import BaseAgent

class ClientOnboardingAgent(BaseAgent):
    def __init__(self):
        super().__init__("Onboarding-Agent")

    def onboard(self, client_name, domain):
        self.log("Onboarding client")
        return {
            "tenant_id": client_name.lower().replace(" ", "_"),
            "domain": domain,
            "features": ["orders", "delivery", "payments"]
        }
