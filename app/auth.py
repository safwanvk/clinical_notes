from fastapi import Request, Header, HTTPException
from typing import Optional
import json

async def get_current_user(
            request: Request,
            authorization: Optional[str] = Header(None)
      ):
      if request.method == "GET":
            return None

      if request.method == "POST":
            try:
                  body = await request.body()
                  parsed = json.loads(body)
                  query = parsed.get("query", "")
                  if "__schema" in query or "IntrospectionQuery" in query:
                        return None
            except Exception:
                  pass

      if not authorization or not authorization.startswith("Bearer "):
            raise HTTPException(status_code=401, detail="Missing or invalid token")

      token = authorization.split("Bearer ")[-1]
      if token != "testtoken":
            raise HTTPException(status_code=403, detail="Invalid token")

      return {"user_id": 1, "role": "admin"}