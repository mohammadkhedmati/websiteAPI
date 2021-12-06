import whois

domain = input("Input domain name : \n ")

domain_info = whois.whois(domain)

# for key in domain_info.keys():
#     print(key)

for key, value in domain_info.items():
    print(key, ':', value)
