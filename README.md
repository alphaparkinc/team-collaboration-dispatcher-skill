# genpark-team-collaboration-dispatcher-skill

> **GenPark AI Agent Skill** -- Multi-agent task planning and routing dispatcher.

## Quick Start

```python
from client import TeamCollaborationDispatcherClient
client = TeamCollaborationDispatcherClient()
res = client.dispatch_task("Analyze code")
print(res["dispatch_plan"])
```
