from fastapi.testclient import TestClient
from main import app

client=TestClient(app)
BASE={"shape":"Oval","carat":1.5,"setting":"solitaire","quote":1850,"certificate_issuer":"IGI","report_number":"LG123456"}

def test_health(): assert client.get("/health").json()=={"status":"ok"}
def test_audit_flags_high_quote():
    result=client.post("/audit",json={**BASE,"quote":4200})
    assert result.status_code==200
    assert result.json()["verdict"]=="high"
    assert result.json()["flags"]
def test_audit_returns_questions_for_normal_quote():
    body=client.post("/audit",json=BASE).json()
    assert body["demo"] is True
    assert len(body["questions"])==3
def test_rejects_bad_report_number():
    result=client.post("/audit",json={**BASE,"report_number":"?"})
    assert result.status_code==422
def test_rejects_out_of_range_quote():
    result=client.post("/audit",json={**BASE,"quote":99})
    assert result.status_code==422
