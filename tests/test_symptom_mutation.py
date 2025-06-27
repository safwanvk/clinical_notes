import pytest
import pytest_asyncio
from app.db import async_session_maker
from .utilities import create_patient, graphql_request
from httpx import ASGITransport, AsyncClient
from app.main import clinical_app


@pytest_asyncio.fixture
async def client():
      transport = ASGITransport(app=clinical_app)
      async with AsyncClient(transport=transport, base_url="http://test") as c:
            yield c

@pytest.mark.asyncio
async def test_add_symptom(client):
      async with async_session_maker() as session:
            patient = await create_patient(session)

      query = f"""
      mutation {{
            addOrUpdateSymptom(input: {{
                  patientId: {patient.id},
                  name: "Headache"
            }}) {{
                  id
                  name
            }}
      }}
      """

      response = await client.post("/graphql", **graphql_request(query))

      assert response.status_code == 200
      data = response.json()

      if "errors" in data:
            raise AssertionError(f"GraphQL error: {data['errors']}")

      assert data["data"]["addOrUpdateSymptom"]["name"] == "Headache"


@pytest.mark.asyncio
async def test_symptom_patient_not_found(client):
      query = """
      mutation {
            addOrUpdateSymptom(input: {
                  patientId: 999,
                  name: "Fever"
            }) {
                  id
                  name
            }
      }
      """

      response = await client.post("/graphql", **graphql_request(query))
      assert "Patient with id 999 not found." in response.text


@pytest.mark.asyncio
async def test_symptom_validation_error(client):
      async with async_session_maker() as session:
            patient = await create_patient(session)

      query = f"""
      mutation {{
            addOrUpdateSymptom(input: {{
                  patientId: {patient.id},
                  name: "A"
            }}) {{
                  id
                  name
            }}
      }}
      """

      response = await client.post("/graphql", **graphql_request(query))
      assert "at least 2 characters" in response.text


@pytest.mark.asyncio
async def test_symptom_without_token(client):
      query = """
      mutation {
            addSymptom(input: {
                  patientId: 1,
                  name: "Cough"
            }) {
                  id
                  name
            }
      }
      """
      response = await client.post("/graphql", **graphql_request(query, token=None))

      assert response.status_code == 403 or response.status_code == 401
      assert "Missing or invalid token" in response.text


@pytest.mark.asyncio
async def test_symptom_invalid_token(client):
      query = """
      mutation {
            addOrUpdateSymptom(input: {
                  patientId: 1,
                  name: "Cough"
            }) {
                  id
                  name
            }
      }
      """
      response = await client.post("/graphql", **graphql_request(query, token="wrongtoken"))
      assert response.status_code == 403
      assert "Invalid token" in response.text