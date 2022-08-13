import requests
from bs4 import BeautifulSoup
import re
from urllib.request import Request, urlopen
from fp.fp import FreeProxy


def html_pars(url):
    base_url = "https://www.wmtips.com/tools/info/"
    domain = url
    check_url = base_url+domain
    cookies = {
        'sc_is_visitor_unique': 'rx3367981.1660377217.B992B83B557C4FFFB14906F463B336AC.2.2.2.2.2.2.2.2.2',
        '_gid': 'GA1.2.2036453768.1660377218',
        '_ga_W8JE4TXSZJ': 'GS1.1.1660377218.2.0.1660377218.0',
        '_ga': 'GA1.1.1757969394.1658670102',
        '__atuvc': '8%7C30%2C0%7C31%2C1%7C32',
        '__atuvs': '62f75882cec68411000',
    }

    headers = {
        'authority': 'www.wmtips.com',
        'accept': 'text/html,application/xhtml+xml,application/xml;q=0.9,image/avif,image/webp,image/apng,*/*;q=0.8,application/signed-exchange;v=b3;q=0.9',
        'accept-language': 'en-US,en;q=0.9,fa;q=0.8',
        'cache-control': 'max-age=0',
        # Requests sorts cookies= alphabetically
        # 'cookie': 'sc_is_visitor_unique=rx3367981.1660377217.B992B83B557C4FFFB14906F463B336AC.2.2.2.2.2.2.2.2.2; _gid=GA1.2.2036453768.1660377218; _ga_W8JE4TXSZJ=GS1.1.1660377218.2.0.1660377218.0; _ga=GA1.1.1757969394.1658670102; __atuvc=8%7C30%2C0%7C31%2C1%7C32; __atuvs=62f75882cec68411000',
        'sec-ch-ua': '"Chromium";v="104", " Not A;Brand";v="99", "Google Chrome";v="104"',
        'sec-ch-ua-mobile': '?0',
        'sec-ch-ua-platform': '"macOS"',
        'sec-fetch-dest': 'document',
        'sec-fetch-mode': 'navigate',
        'sec-fetch-site': 'none',
        'sec-fetch-user': '?1',
        'upgrade-insecure-requests': '1',
        'user-agent': 'Mozilla/5.0 (Macintosh; Intel Mac OS X 10_15_7) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/104.0.0.0 Safari/537.36',
    }
    print("proxxy .... ")
    proxy = FreeProxy(anonym=True).get()
    print(proxy)
    proxies = {
        'http': proxy,
        'https': proxy,
    }
    ip2 = requests.get('https://httpbin.org/ip', proxies=proxies).text
    print(ip2)
    response = requests.get(
        check_url, headers=headers, proxies=proxies)
    print(response)
    print(response.headers['content-type'])

    soup = BeautifulSoup(response.text, 'html.parser')
    return soup


def html_pars_likody(url, chekcer):
    base_url_linkody = "http://bc.linkody.com/en/seo-tools/{}/".format(chekcer)
    domain_linkody = url + '?' + '/'
    check_url_linkody = base_url_linkody+domain_linkody
    page_linkody = requests.get(check_url_linkody).text
    soup_linkody = BeautifulSoup(page_linkody, 'html.parser')
    return soup_linkody


def all_info(url):
    items = [
        web_description, page_information, website_information, Technologies,
        Rankings, Linking_information, social, Estimated_traffic,
        On_page_data_headings, On_page_data_links, On_page_data_images,
        Top_ranking_keywords, Competitors, Domain_whois, IP_whois,
        Websites_on_IP, Subdomains, Backlinks_report, Website_Rating, website_authority
    ]
    items_str = [
        'web_description', 'page_information', 'website_information', 'Technologies',
        'Rankings', 'Linking_information', 'social', 'Estimated_traffic',
        'On_page_data_headings', 'On_page_data_links', 'On_page_data_images',
        'Top_ranking_keywords', 'Competitors', 'Domain_whois', 'IP_whois',
        'Websites_on_IP', 'Subdomains', 'Backlinks_report', 'Website_Rating', 'website_authority'
    ]
    allinfo = {}
    soup_all = html_pars(url)
    for item, item_str in zip(items, items_str):
        try:
            res = item(url, soup_data=soup_all, useable=True)
            allinfo[item_str] = res
        except:
            try:
                url = 'www.'
                res = item(url, soup_data=soup_all, useable=True)
                allinfo[item_str] = res
            except:
                allinfo[item_str] = None
            pass

    return allinfo


def web_description(url, soup_data=None, useable=False):
    if useable == True:
        soup = soup_data
    else:
        soup = html_pars(url)
    try:
        page_info_sec = soup.find("div", {"class": "flex"})
        page_disc = page_info_sec.find_all("p")
    except:
        return {
            None
        }
    para = ''
    for paragraph in page_disc:
        temp = paragraph.text.strip()
        para = para + temp
    words = para.split(' ')
    ranks_arr = []
    for word in words:
        if "#" in word:
            ranks_arr.append(word)
    parag = {
        'disc': para,
    }
    try:
        parag['world'] = ranks_arr[0]
        parag['iran'] = ranks_arr[1]
    except:
        parag['world'] = None
        parag['iran'] = None
    return parag


def page_information(url, soup_data=None, useable=False):
    if useable == True:
        soup = soup_data
    else:
        soup = html_pars(url)
    try:
        page_info_sec = soup.find("section", {"id": "page"})
        page_info_tbl = page_info_sec.find("table")
    except:
        return {
            None
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


def website_information(url, soup_data=None, useable=False):
    if useable == True:
        soup = soup_data
    else:
        soup = html_pars(url)

    try:
        page_info_sec = soup.find("section", {"id": "site"})
        page_info_tbl = page_info_sec.find("table")
    except:
        return {
            'status': 400,
            'error': 'Not Found'
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


def Technologies(url, soup_data=None, useable=False):
    if useable == True:
        soup = soup_data
    else:
        soup = html_pars(url)

    try:
        page_info_sec = soup.find("section", {"id": "techs"})
        page_info_tbl = page_info_sec.find("table")
    except:
        return {
            None
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


def Rankings(url, soup_data=None, useable=False):
    if useable == True:
        soup = soup_data
    else:
        soup = html_pars(url)
    # print(soup)
    try:
        page_info_sec = soup.find("section", {"id": "ranks"})
        page_info_div = page_info_sec.find("div", {"class": "charts"})
        # print(page_info_div)
    except:
        return {
            None
        }
    ranking_info = {}
    for sibling in page_info_div.div.next_siblings:
        try:
            s = sibling.findChildren()
            s[0].find("div", {"class": "tooltip"}).decompose()
            name = s[0].text.strip()
            for siblings in sibling.div.next_siblings:
                value = siblings.text.strip()
            ranking_info[name] = value
        except:
            pass

    return ranking_info


def Linking_information(url, soup_data=None, useable=False):
    if useable == True:
        soup = soup_data
    else:
        soup = html_pars(url)

    try:
        page_info_sec = soup.find("section", {"id": "seo"})
        page_info_div = page_info_sec.find("div", {"class": "charts"})
    except:
        return {
            None
        }
    link_info = {}
    for sibling in page_info_div.div.next_siblings:
        try:
            s = sibling.findChildren()
            s[0].find("div", {"class": "tooltip"}).decompose()
            name = s[0].text.strip()
            for siblings in sibling.div.next_siblings:
                value = siblings.text.strip()
            link_info[name] = value
        except:
            pass

    return link_info


def social(url, soup_data=None, useable=False):
    if useable == True:
        soup = soup_data
    else:
        soup = html_pars(url)

    try:
        page_info_sec = soup.find("section", {"id": "social"})
        page_info_div = page_info_sec.find("div", {"class": "charts"})
    except:
        return {
            None
        }
    social_acc = {}
    for sibling in page_info_div.div.next_siblings:
        try:
            s = sibling.findChildren()
            s[0].find("div", {"class": "tooltip"}).decompose()
            name = s[0].text.strip()
            # print(name)
            for siblings in sibling.div.next_siblings:
                value = siblings.text.strip()
                # print(value)
            social_acc[name] = value
        except:
            pass
    return social_acc


def Estimated_traffic(url, soup_data=None, useable=False):
    if useable == True:
        soup = soup_data
    else:
        soup = html_pars(url)

    try:
        page_info_sec = soup.find("section", {"id": "traffic"})
        page_info_tbl = page_info_sec.find("table")
    except:
        return {
            None
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


def On_page_data_headings(url, soup_data=None, useable=False):
    if useable == True:
        soup = soup_data
    else:
        soup = html_pars(url)

    try:
        page_info_sec = soup.find("section", {"id": "onpage"})
        page_info_div = page_info_sec.find("div", {"id": "headings"})
        page_info_tbl = page_info_div.find("table")
    except:
        return {
            None
        }

    rows = page_info_tbl.find_all('tr')
    names = rows[0].find_all('th')
    values = rows[1].find_all('td')
    values_per = []
    try:
        values_percent = rows[1].find_all('span')
        for val in values_percent:
            values_per.append(val.text.strip())
    except:
        pass
    heading = {}
    if len(values_per) == 0:
        for col, value in zip(names, values):
            name = col.text.strip()
            try:
                value.find("span").decompose()
            except:
                pass
            value = value.text.strip()
            heading[name] = value
    else:
        for col, value, vals in zip(names, values, values_per):
            name = col.text.strip()
            try:
                value.find("span").decompose()
            except:
                pass
            value = value.text.strip()
            heading[name] = value, vals

    return heading


def On_page_data_links(url, soup_data=None, useable=False):
    if useable == True:
        soup = soup_data
    else:
        soup = html_pars(url)

    try:
        page_info_sec = soup.find("section", {"id": "onpage"})
        page_info_div = page_info_sec.find("div", {"id": "links"})
        page_info_tbl = page_info_div.find("table")
    except:
        return {
            None
        }
    rows = page_info_tbl.find_all('tr')
    links = {}
    for col in rows:
        name = col.find('th')
        try:
            name.find("div", {"class": "tooltip"}).decompose()
        except:
            pass
        value = col.find('td')
        name = name.text.strip()
        value = value.text.strip()
        links[name] = value

    return links


def On_page_data_images(url, soup_data=None, useable=False):
    if useable == True:
        soup = soup_data
    else:
        soup = html_pars(url)

    try:
        page_info_sec = soup.find("section", {"id": "onpage"})
        page_info_div = page_info_sec.find("div", {"id": "images"})
        page_info_tbl = page_info_div.find("table")
    except:
        return {
            None
        }
    rows = page_info_tbl.find_all('tr')
    images = {}
    for col in rows:
        name = col.find('th')
        try:
            name.find("div", {"class": "tooltip"}).decompose()
        except:
            pass
        value = col.find('td')
        name = name.text.strip()
        value = value.text.strip()
        images[name] = value

    return images


def Top_ranking_keywords(url, soup_data=None, useable=False):
    if useable == True:
        soup = soup_data
    else:
        soup = html_pars(url)

    try:
        page_info_sec = soup.find("section", {"id": "semtop"})
        page_info_tbl = page_info_sec.find("table")
        rows = page_info_tbl.find_all('tr')
    except:
        return {
            None
        }
    keywords = {}
    keywords["keyword"] = "Position_in_Google", "Volume_per_month", "CPC"
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
            keywords[keyword] = Position_in_Google, Volume_per_month, CPC
        except:
            pass
    return keywords


def Competitors(url, soup_data=None, useable=False):
    if useable == True:
        soup = soup_data
    else:
        soup = html_pars(url)

    try:
        page_info_sec = soup.find("section", {"id": "semcomp"})
        page_info_tbl = page_info_sec.find("table")
    except:
        return {
            None
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
        except:
            pass
    return competits


def Domain_whois(url, soup_data=None, useable=False):
    if useable == True:
        soup = soup_data
    else:
        soup = html_pars(url)

    try:
        page_info_sec = soup.find("section", {"id": "whois"})
        page_info_tbl = page_info_sec.find("table")
    except:
        return {
            'status': 400,
            'error': 'Not Found'
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


def IP_whois(url, soup_data=None, useable=False):
    if useable == True:
        soup = soup_data
    else:
        soup = html_pars(url)

    try:
        page_info_sec = soup.find("section", {"id": "ipwhois"})
        page_info_tbl = page_info_sec.find("table")
    except:
        return {
            'status': 400,
            'error': 'Not Found'
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


def Websites_on_IP(url, soup_data=None, useable=False):
    if useable == True:
        soup = soup_data
    else:
        soup = html_pars(url)

    try:
        page_info_sec = soup.find("section", {"id": "onip"})
        page_info_div = page_info_sec.find_all("a")
    except:
        return {
            None
        }
    onip = {}
    onip["subdomains"] = page_info_sec.find("h2").text.strip()
    most = []

    for el in page_info_div:
        most.append(el.text.strip())

    onip["most"] = most

    return onip


def Subdomains(url, soup_data=None, useable=False):
    if useable == True:
        soup = soup_data
    else:
        soup = html_pars(url)

    try:
        page_info_sec = soup.find("section", {"id": "sub"})
        page_info_div = page_info_sec.find_all("a")
    except:
        return {
            None
        }
    subs = {}
    subs["subdomains"] = page_info_sec.find("h2").text.strip()
    most = []

    for el in page_info_div:
        most.append(el.text.strip())

    subs["most"] = most
    return subs

# Linkody


def Backlinks_report(url,):
    soup_linkody = html_pars_likody(url, "free-backlink-checker")
    try:
        page_info_tbl = soup_linkody.find("table", {"class": "simple"})
        rows = page_info_tbl.find('tr')
        cols = rows.find_all('td')
    except:
        return {
            None
        }
    backlinks = {}
    idx = 0
    for col in cols:
        name = col.find("div", {"class": "name"})
        name = name.text.strip()
        if idx == 0:
            value = col.find('div', attrs={
                             "style": "position: absolute; left: 50%; top: 0; margin-top: 80px; font-size: 30px; margin-left: -16px; width: 32px;"})
            value = value.text.strip()
        else:
            value = col.find("div", {"class": "number"})
            value = value.text.strip()
        backlinks[name] = value
        idx += 1

    return backlinks


def Website_Rating(url):
    soup_linkody = html_pars_likody(url, "free-backlink-checker")
    try:
        page_info_div = soup_linkody.find("div", {"class": "row"})
        names = page_info_div.find_all("div", {"class": "name"})
        values = page_info_div.find_all("div", {"class": "number"})
    except:
        return {
            None
        }
    web_rate = {}
    for name, value in zip(names, values):
        name = name.text.strip()
        value = value.text.strip()
        web_rate[name] = value

    return web_rate


def website_authority(url):
    soup_linkody = html_pars_likody(url, "website-authority")
    try:
        page_info_div = soup_linkody.find("div", {"class": "row"})
        names = page_info_div.find_all("div", {"class": "name"})
        values = page_info_div.find_all("div", {"class": "number"})
    except:
        return {
            None
        }
    web_authority = {}
    for name, value in zip(names, values):
        name = name.text.strip()
        value = value.text.strip()
        web_authority[name] = value

    return web_authority
