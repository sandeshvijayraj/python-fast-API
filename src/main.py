from fastapi import FastAPI, HTTPException
from handlers.jira import Jira

from models.apiModels import PutJiraTicket

app = FastAPI()

def authoriser():
    # get token from headers using Request in fastapi. Similar to flask
    return True

@app.put('/jiraTicket')
async def create_ticket(item: PutJiraTicket):
    # Call to ots respective handler function in handlers
    jira_handler = Jira()
    if not authoriser():
        raise HTTPException(401)
    data = await jira_handler.createJiraTicket(item)
    return data

