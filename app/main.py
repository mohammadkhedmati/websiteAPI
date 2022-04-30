from fastapi import FastAPI
from app import scraper
from app import data
from pydantic import BaseModel


class allinfo(BaseModel):
    url: str

class domain(BaseModel):
    url: str

description = """
Website API helps you to get website SEO details. 🚀
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


#@app.post("/allinfo/")
#async def allinfo(item: allinfo):
#    resp = scraper.AllInfo(item.url)
#    return resp

@app.post("/page_information/")
async def page_information(item: domain):
    resp = data.page_information(item.url)
    return resp


@app.post("/website_information/")
async def website_information(item: domain):
    resp = data.website_information(item.url)
    return resp

@app.post("/Technologies/")
async def Technologies(item: domain):
    resp = data.Technologies(item.url)
    return resp

@app.post("/Ranking/")
async def Ranking(item: domain):
    resp = data.Rankings(item.url)
    return resp

@app.post("/Linking/")
async def Linking(item: domain):
    resp = data.Linking_information(item.url)
    return resp

@app.post("/social/")
async def social(item: domain):
    resp = data.social(item.url)
    return resp
 
@app.post("/traffic/")
async def traffic(item: domain):
    resp = data.Estimated_traffic(item.url)
    return resp

@app.post("/onpage_headings/")
async def onpage_headings(item: domain):
    resp = data.On_page_data_headings(item.url)
    return resp

@app.post("/onpage_links/")
async def onpage_links(item: domain):
    resp = data.On_page_data_links(item.url)
    return resp

@app.post("/onpage_images/")
async def onpage_images(item: domain):
    resp = data.On_page_data_images(item.url)
    return resp

@app.post("/Topkeywords/")
async def Topkeywords(item: domain):
    resp = data.Top_ranking_keywords(item.url)
    return resp

@app.post("/compatitors/")
async def compatitors(item: domain):
    resp = data.Competitors(item.url)
    return resp

@app.post("/domain_whois/")
async def domain_whois(item: domain):
    resp = data.Domain_whois(item.url)
    return resp

@app.post("/whois/")
async def whois(item: domain):
    resp = data.IP_whois(item.url)
    return resp

@app.post("/onIP/")
async def onIP(item: domain):
    resp = data.Websites_on_IP(item.url)
    return resp

@app.post("/subdomains/")
async def subdomains(item: domain):
    resp = data.Subdomains(item.url)
    return resp

#linkody
@app.post("/backlins/")
async def backlins(item: domain):
    resp = data.Backlinks_report(item.url)
    return resp

@app.post("/web_rate/")
async def web_rate(item: domain):
    resp = data.Website_Rating(item.url)
    return resp