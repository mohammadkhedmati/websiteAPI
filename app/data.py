import requests 
from bs4 import BeautifulSoup
import re



def page_information(url):
    base_url="https://www.wmtips.com/tools/info/"
    domain = 'www.' + url 
    check_url=base_url+domain

    # request formatted url for rank
    page=requests.get(check_url).text
    soup=BeautifulSoup(page, 'html.parser')
    try:
        page_info_sec = soup.find("section", { "id" : "page" })
        page_info_tbl = page_info_sec.find("table")
    except :
        return {
            'status' : 400,
            'error' : 'Not Found'
        }
    
    rows = page_info_tbl.find_all('tr')
    page_information = {}
    for col in rows:
        name = col.find('th')
        value = col.find('td')
        name = name.text.strip()
        value = value.text.strip()
        page_information[name] = value

    return page_information

def website_information(url):
    base_url="https://www.wmtips.com/tools/info/"
    domain = 'www.' + url 
    check_url=base_url+domain

    # request formatted url for rank
    page=requests.get(check_url).text
    soup=BeautifulSoup(page, 'html.parser')
    try:
        page_info_sec = soup.find("section", { "id" : "site" })
        page_info_tbl = page_info_sec.find("table")
    except :
            return {
                'status' : 400,
                'error' : 'Not Found'
            }
    rows = page_info_tbl.find_all('tr')
    web_information = {}
    for col in rows:
        name = col.find('th')
        value = col.find('td')
        name = name.text.strip()
        value = value.text.strip()
        web_information[name] = value

    return web_information

def Technologies(url):
    base_url="https://www.wmtips.com/tools/info/"
    domain = 'www.' + url 
    check_url=base_url+domain

    # request formatted url for rank
    page=requests.get(check_url).text
    soup=BeautifulSoup(page, 'html.parser')
    try:
        page_info_sec = soup.find("section", { "id" : "techs" })
        page_info_tbl = page_info_sec.find("table")
    except :
        return {
            'status' : 400,
            'error' : 'Not Found'
        }
    rows = page_info_tbl.find_all('tr')
    # count_children = len(page_info_tbl.find_all('tr')) number of children
    Technologies_info = {}
    for col in rows:
        name = col.find('th')
        value = col.find('td')
        name = name.text.strip()
        value = value.text.strip()
        Technologies_info[name] = value

    return Technologies_info

def Rankings(url):
    base_url="https://www.wmtips.com/tools/info/"
    domain = 'www.' + url 
    check_url=base_url+domain

    # request formatted url for rank
    page=requests.get(check_url).text
    soup=BeautifulSoup(page, 'html.parser')
    try:
        page_info_sec = soup.find("section", { "id" : "ranks" })
        page_info_div = page_info_sec.find("div", {"class" : "charts"})
    except :
        return {
            'status' : 400,
            'error' : 'Not Found'
        }
    ranking_info = {}
    for sibling in page_info_div.div.next_siblings:
        try:
            s = sibling.findChildren()
            s[0].find("div", {"class" : "tooltip"}).decompose()
            name = s[0].text.strip()
            # print(name)
            for siblings in sibling.div.next_siblings:
                value = siblings.text.strip()
                # print(value)
            ranking_info[name] = value
        except :
            pass    

    return ranking_info

def Linking_information(url):
    base_url="https://www.wmtips.com/tools/info/"
    domain = 'www.' + url 
    check_url=base_url+domain
    page=requests.get(check_url).text
    soup=BeautifulSoup(page, 'html.parser')
    try:
        page_info_sec = soup.find("section", { "id" : "seo" })
        page_info_div = page_info_sec.find("div", {"class" : "charts"})
    except :
        return {
            'status' : 400,
            'error' : 'Not Found'
        }
    link_info = {}
    for sibling in page_info_div.div.next_siblings:
        try:
            s = sibling.findChildren()
            s[0].find("div", {"class" : "tooltip"}).decompose()
            name = s[0].text.strip()
            # print(name)
            for siblings in sibling.div.next_siblings:
                value = siblings.text.strip()
                # print(value)
            link_info[name] = value
        except :
            pass   

    return link_info

def social(url):
    base_url="https://www.wmtips.com/tools/info/"
    domain = 'www.' + url 
    check_url=base_url+domain
    page=requests.get(check_url).text
    soup=BeautifulSoup(page, 'html.parser')
    try:
        page_info_sec = soup.find("section", { "id" : "social" })
        page_info_div = page_info_sec.find("div", {"class" : "charts"})
    except :
        return {
            'status' : 400,
            'error' : 'Not Found'
        }
    social_acc = {}
    for sibling in page_info_div.div.next_siblings:
        try:
            s = sibling.findChildren()
            s[0].find("div", {"class" : "tooltip"}).decompose()
            name = s[0].text.strip()
            # print(name)
            for siblings in sibling.div.next_siblings:
                value = siblings.text.strip()
                # print(value)
            social_acc[name] = value
        except :
            pass
    return social_acc

def Estimated_traffic(url):
    base_url="https://www.wmtips.com/tools/info/"
    domain = 'www.' + url 
    check_url=base_url+domain

    # request formatted url for rank
    page=requests.get(check_url).text
    soup=BeautifulSoup(page, 'html.parser')
    try:
        page_info_sec = soup.find("section", { "id" : "traffic" })
        page_info_tbl = page_info_sec.find("table")
    except :
        return {
            'status' : 400,
            'error' : 'Not Found'
        }
    rows = page_info_tbl.find_all('tr')
    traffic_information = {}
    for col in rows:
        name = col.find('th')
        value = col.find('td')
        name = name.text.strip()
        value = value.text.strip()
        traffic_information[name] = value

    return traffic_information

def On_page_data_headings(url):
    base_url="https://www.wmtips.com/tools/info/"
    domain = 'www.' + url 
    check_url=base_url+domain

    # request formatted url for rank
    page=requests.get(check_url).text
    soup=BeautifulSoup(page, 'html.parser')
    try:
        page_info_sec = soup.find("section", { "id" : "onpage" })
        page_info_div = page_info_sec.find("div", {"id" : "headings"})
        page_info_tbl = page_info_div.find("table")
    except :
        return {
            'status' : 400,
            'error' : 'Not Found'
        }

    rows = page_info_tbl.find_all('tr')
    names = rows[0].find_all('th')
    values = rows[1].find_all('td')
    values_per = []
    try:
        values_percent = rows[1].find_all('span')
        for val in values_percent:
            values_per.append(val.text.strip())
    except :
        pass
    heading = {}
    if len(values_per) == 0 :
        for col,value in zip(names,values):
            name = col.text.strip()
            try:
                value.find("span").decompose()
            except :
                pass
            value = value.text.strip()
            heading[name] = value
    else:
        for col,value,vals in zip(names,values,values_per):
            name = col.text.strip()
            try:
                value.find("span").decompose()
            except :
                pass
            value = value.text.strip()
            heading[name] = value,vals

    return heading

def On_page_data_links(url):
    base_url="https://www.wmtips.com/tools/info/"
    domain = 'www.' + url 
    check_url=base_url+domain

    # request formatted url for rank
    page=requests.get(check_url).text
    soup=BeautifulSoup(page, 'html.parser')
    try:
        page_info_sec = soup.find("section", { "id" : "onpage" })
        page_info_div = page_info_sec.find("div", {"id" : "links"})
        page_info_tbl = page_info_div.find("table")
    except :
        return {
            'status' : 400,
            'error' : 'Not Found'
        }
    rows = page_info_tbl.find_all('tr')
    links = {}
    for col in rows:
        name = col.find('th')
        try:
            name.find("div", {"class" : "tooltip"}).decompose()
        except :
            pass
        value = col.find('td')
        name = name.text.strip()
        value = value.text.strip()
        links[name] = value
        
    return links

def On_page_data_images(url):
    base_url="https://www.wmtips.com/tools/info/"
    domain = 'www.' + url 
    check_url=base_url+domain

    # request formatted url for rank
    page=requests.get(check_url).text
    soup=BeautifulSoup(page, 'html.parser')
    try:
        page_info_sec = soup.find("section", { "id" : "onpage" })
        page_info_div = page_info_sec.find("div", {"id" : "images"})
        page_info_tbl = page_info_div.find("table")
    except :
        return {
            'status' : 400,
            'error' : 'Not Found'
        }
    rows = page_info_tbl.find_all('tr')
    images = {}
    for col in rows:
        name = col.find('th')
        try:
            name.find("div", {"class" : "tooltip"}).decompose()
        except :
            pass
        value = col.find('td')
        name = name.text.strip()
        value = value.text.strip()
        images[name] = value
        
    return images

def Top_ranking_keywords(url):
    base_url="https://www.wmtips.com/tools/info/"
    domain = 'www.' + url 
    check_url=base_url+domain

    # request formatted url for rank
    page=requests.get(check_url).text
    soup=BeautifulSoup(page, 'html.parser')
    try:
        page_info_sec = soup.find("section", { "id" : "semtop" })
        page_info_tbl = page_info_sec.find("table")
    except :
        return {
            'status' : 400,
            'error' : 'Not Found'
        }
    rows = page_info_tbl.find_all('tr')
    keywords = {}
    keywords["keyword"] = "Position_in_Google","Volume_per_month","CPC"
    for el in rows:
        try:
            cols = el.find_all('td')
            keyword = cols[0]
            Position_in_Google = cols[1]
            Volume_per_month = cols[2]
            CPC = cols[3]
            keyword = keyword.text.strip()
            Position_in_Google = Position_in_Google.text.strip()
            Volume_per_month = Volume_per_month.text.strip()
            CPC = CPC.text.strip()
            keywords[keyword] = Position_in_Google,Volume_per_month,CPC
        except :
            pass
    return keywords

def Competitors(url):
    base_url="https://www.wmtips.com/tools/info/"
    domain = 'www.' + url 
    check_url=base_url+domain

    # request formatted url for rank
    page=requests.get(check_url).text
    soup=BeautifulSoup(page, 'html.parser')
    try:
        page_info_sec = soup.find("section", { "id" : "semcomp" })
        page_info_tbl = page_info_sec.find("table")
    except :
        return {
            'status' : 400,
            'error' : 'Not Found'
        }
    rows = page_info_tbl.find_all('tr')
    competits = {}
    for el in rows:
        try:
            cols = el.find_all('td')
            name = cols[0]
            value = cols[1]
            name = name.text.strip()
            value = value.text.strip()
            competits[name] = value
        except :
            pass
    return competits

def Domain_whois(url):
    base_url="https://www.wmtips.com/tools/info/"
    domain = 'www.' + url 
    check_url=base_url+domain

    # request formatted url for rank
    page=requests.get(check_url).text
    soup=BeautifulSoup(page, 'html.parser')
    try:
        page_info_sec = soup.find("section", { "id" : "whois" })
        page_info_tbl = page_info_sec.find("table")
    except :
            return {
                'status' : 400,
                'error' : 'Not Found'
            }
    rows = page_info_tbl.find_all('tr')
    domainwhois = {}
    for col in rows:
        name = col.find('th')
        value = col.find('td')
        name = name.text.strip()
        value = value.text.strip()
        domainwhois[name] = value

    return domainwhois

def IP_whois(url):
    base_url="https://www.wmtips.com/tools/info/"
    domain = 'www.' + url 
    check_url=base_url+domain

    # request formatted url for rank
    page=requests.get(check_url).text
    soup=BeautifulSoup(page, 'html.parser')
    try:
        page_info_sec = soup.find("section", { "id" : "ipwhois" })
        page_info_tbl = page_info_sec.find("table")
    except :
            return {
                'status' : 400,
                'error' : 'Not Found'
            }
    rows = page_info_tbl.find_all('tr')
    whois = {}
    for col in rows:
        name = col.find('th')
        value = col.find('td')
        name = name.text.strip()
        value = value.text.strip()
        whois[name] = value

    return whois

def Websites_on_IP(url):
    base_url="https://www.wmtips.com/tools/info/"
    domain = 'www.' + url 
    check_url=base_url+domain

    # request formatted url for rank
    page=requests.get(check_url).text
    soup=BeautifulSoup(page, 'html.parser')
    try:
        page_info_sec = soup.find("section", { "id" : "onip" })
        page_info_div = page_info_sec.find_all("a")
    except :
        return {
            'status' : 400,
            'error' : 'Not Found'
        }
    onip = {}
    onip["subdomains"] = page_info_sec.find("h2").text.strip()
    most = []

    for el in page_info_div:
        most.append(el.text.strip())

    onip["most"] = most
    
    return onip

def Subdomains(url):
    base_url="https://www.wmtips.com/tools/info/"
    domain = 'www.' + url 
    check_url=base_url+domain

    # request formatted url for rank
    page=requests.get(check_url).text
    soup=BeautifulSoup(page, 'html.parser')
    try:
        page_info_sec = soup.find("section", { "id" : "sub" })
        page_info_div = page_info_sec.find_all("a")
    except :
        return {
            'status' : 400,
            'error' : 'Not Found'
        }
    subs = {}
    subs["subdomains"] = page_info_sec.find("h2").text.strip()
    most = []

    for el in page_info_div:
        most.append(el.text.strip())

    subs["most"] = most
    return subs

#Linkody
def Backlinks_report(url):
    base_url="http://bc.linkody.com/en/seo-tools/free-backlink-checker/"
    domain = url + '?' + '/'
    check_url=base_url+domain
    # request formatted url for rank
    page=requests.get(check_url).text
    soup=BeautifulSoup(page, 'html.parser')
    try:
        page_info_tbl = soup.find("table", {"class" : "simple"})
    except :
        return {
            'status' : 400,
            'error' : 'Not Found'
        }
    rows = page_info_tbl.find('tr')
    cols = rows.find_all('td')
    backlinks = {}
    idx = 0
    for col in cols:
        name = col.find("div", {"class": "name"})
        name = name.text.strip()
        if idx == 0:
            value = col.find('div', attrs={"style" :"position: absolute; left: 50%; top: 0; margin-top: 80px; font-size: 30px; margin-left: -16px; width: 32px;"})
            value = value.text.strip()
        else:
            value = col.find("div", {"class": "number"})
            value = value.text.strip()
        backlinks[name] = value
        idx += 1

    return backlinks

def Website_Rating(url):
    base_url="http://bc.linkody.com/en/seo-tools/free-backlink-checker/"
    domain = url
    check_url=base_url+domain
    # request formatted url for rank
    page=requests.get(check_url).text
    soup=BeautifulSoup(page, 'html.parser')
    try:
        page_info_div = soup.find("div", {"class" : "row"})
    except :
        return {
            'status' : 400,
            'error' : 'Not Found'
        }
    names = page_info_div.find_all("div", {"class" : "name"})
    values = page_info_div.find_all("div", {"class" : "number"})
    web_rate = {}
    for name,value in zip(names,values):
        name = name.text.strip()
        value = value.text.strip()
        web_rate[name] = value

    return web_rate

def website_authority(url):
    base_url="https://www.linkody.com/en/seo-tools/website-authority/"
    domain = url
    check_url=base_url+domain
    # request formatted url for rank
    page=requests.get(check_url).text
    soup=BeautifulSoup(page, 'html.parser')
    try:
        page_info_div = soup.find("div", {"class" : "row"})
    except :
        return {
            'status' : 400,
            'error' : 'Not Found'
        }
    names = page_info_div.find_all("div", {"class" : "name"})
    values = page_info_div.find_all("div", {"class" : "number"})
    web_authority = {}
    for name,value in zip(names,values):
        name = name.text.strip()
        value = value.text.strip()
        web_authority[name] = value

    return web_authority