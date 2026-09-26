import json
from pathlib import Path
from typing import Literal
from fastapi import FastAPI, HTTPException
from pydantic import BaseModel, Field

DATA=json.loads((Path(__file__).parent.parent/"data"/"benchmarks.json").read_text())
app=FastAPI(title="StoneSignal demo API",version="0.1.0")

class AuditRequest(BaseModel):
    shape: Literal["Round","Oval","Emerald"]
    carat: float=Field(ge=0.8,le=2.2)
    setting: Literal["solitaire","halo","three-stone"]
    quote: int=Field(ge=300,le=15000)
    certificate_issuer: str=Field(min_length=2,max_length=12)
    report_number: str=Field(min_length=5,max_length=24,pattern=r"^[A-Za-z0-9-]+$")

def audit_quote(item: AuditRequest):
    candidates=[b for b in DATA["benchmarks"] if b["shape"]==item.shape]
    benchmark=min(candidates,key=lambda b:abs(b["carat"]-item.carat))
    scale=item.carat/benchmark["carat"]
    low=round(benchmark["low"]*scale+DATA["settingAllowance"][item.setting])
    high=round(benchmark["high"]*scale+DATA["settingAllowance"][item.setting])
    flags=[]
    if item.certificate_issuer.upper() not in DATA["certificateIssuers"]: flags.append("Certificate issuer needs independent verification")
    if item.quote>high*1.2: flags.append("Quote is more than 20% above the demo comparison band")
    if item.quote<low*0.75: flags.append("Price is unusually low; verify stone identity and return terms")
    delta=item.quote-high if item.quote>high else item.quote-low if item.quote<low else 0
    verdict="high" if item.quote>high else "suspiciously-low" if item.quote<low*0.75 else "within-band" if item.quote>=low else "low"
    return {"verdict":verdict,"band":{"low":low,"high":high},"delta":delta,"flags":flags,"questions":["Can I verify the report number on the issuer website?","Is the stone inscription visible under magnification?","What are the written return and resize terms?"],"demo":True}

@app.get("/health")
def health(): return {"status":"ok"}

@app.post("/audit")
def audit(item:AuditRequest):
    try: return audit_quote(item)
    except (KeyError,ValueError) as exc: raise HTTPException(status_code=422,detail="Unsupported ring configuration") from exc
