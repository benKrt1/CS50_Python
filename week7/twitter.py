import re

url = input("URL: ").strip()

#username = url.replace("https://twitter.com/", "")
#username = url.removeprefix("https://twitter.com/")
#username = re.sub(r"^(https?://)?(www\.)linkedin\.com/in?/?", "", url)
#if matches := re.search(r"^https?://(www\.)?linkedin\.com/in/(.+)/$", url, re.IGNORECASE):
    #print(f"Username: ", matches.group(2))

if matches := re.search(r"^https?://(?:www\.)?linkedin\.com/in/([a-z0-9_]+)/$", url, re.IGNORECASE):
    print(f"Username: ", matches.group(1))
