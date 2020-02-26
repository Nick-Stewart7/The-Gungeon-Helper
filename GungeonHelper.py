import requests
url = requests.get("https://enterthegungeon.gamepedia.com/Guns").text



#from bs4 import beautifulsoup4

#Gunsoup = BeautifulSoup(url)
gunTable = Gunsoup.find("table",{"class":"wikitable sortable"})
weplist = gunTable.findAll("tr")

GunList = []

for i in range(len(weplist)):
    stats = []
    for node in weplist[i].findAll("td"):
        stat = ''.join(node.findAll(text=True))
        stat = stat.strip()
        stat = stat.strip('\n')

        if stat != '':
            stats.append(stat)
    for node in weplist[i].findAll('img'):
        stat = ''.join(node["alt"])
        if stat != None:
            if(stat[-4:] == ".png"):
                stat = stat[:-4]
            if stat not in stats:
                stats.append(stat)
    if(stats != []):
        GunList.append(stats)
print(GunList)
for stat in GunList[16]:
    print(stat)
print(Gunsoup.prettify())
for stat in GunList[0]:
    print(stat)
for stat in GunList[1]:
    print(stat)
for stat in GunList[-1]:
    print(stat)