from models.apiModels import PutJiraTicket
from fastapi import HTTPException

class Jira:
    async def createJiraTicket(self, input: PutJiraTicket):
        # No need for validations
        try:
            # Call to middleware. can also do some transformation if needed.
            return {"messag": input}
        except:
            raise HTTPException(status_code=500, detail={"message": "Internal server error. Contact administrator"})