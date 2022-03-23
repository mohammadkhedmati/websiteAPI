from fastapi import FastAPI
from app import scraper
from pydantic import BaseModel
from seoanalyzer import analyze


class allinfo(BaseModel):
    url: str

class seoanalyz(BaseModel):
    url: str

class googleapi(BaseModel):
    url: str

description = """
Instagram API helps you to get website SEO details. 🚀
"""
app = FastAPI(
    title="Website API",
    description=description,
    version="0.0.1",
    terms_of_service="https://faraabin.com/",
    contact={
        "name": "mohammad khedmati",
        "url": "https://mkhedmati.ir",
        "email": "mohammad.khedmati2012@gmail.com",
    },
    license_info={
        "name": "Apache 2.0",
        "url": "https://www.apache.org/licenses/LICENSE-2.0.html",
    },
)



@app.get("/")
async def root():
    return "hello dear !"


@app.post("/allinfo/")
async def allinfo(item: allinfo):
    resp = scraper.AllInfo(item.url)
    return resp

@app.post("/seo_analyze/")
async def seoanalyze(item: seoanalyz):
    output = analyze(item.url, analyze_headings=True, analyze_extra_tags=True)
    return output

@app.post("/google_api/")
async def google_api(item: googleapi):
    resp = scraper.google_api(item.url)
    return resp