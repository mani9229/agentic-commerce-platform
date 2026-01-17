class AgentEvaluation:
    def __init__(self):
        self.records = []

    def log(self, agent, task, success):
        self.records.append({
            "agent": agent,
            "task": task,
            "success": success
        })

    def summary(self):
        total = len(self.records)
        success = sum(1 for r in self.records if r["success"])
        return {"total": total, "success_rate": success / total if total else 0}
