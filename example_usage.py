"""
example_usage.py -- Demonstrates TeamCollaborationDispatcherClient
"""
from client import TeamCollaborationDispatcherClient

def main():
    client = TeamCollaborationDispatcherClient()
    result = client.dispatch_task("Write a new promotional email draft")
    print("[Team Dispatch Plan]")
    for step in result['dispatch_plan']:
        print(f"Step: {step['phase']} -> Assigned: {step['assigned_agent']}")

if __name__ == "__main__":
    main()
