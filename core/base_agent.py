from modes.mock import MODE

class BaseAgent:
    def __init__(self, name, tenant=None):
        self.name = name
        self.tenant = tenant

    def log(self, message):
        tenant_id = self.tenant.tenant_id if self.tenant else "default"
        print(f"[{self.name} | {MODE} | {tenant_id}] {message}")

    def is_mock(self):
        return MODE == "MOCK"
