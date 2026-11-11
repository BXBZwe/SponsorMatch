import csv

with open ("/home/bxbzwe/projects/SponsorMatch/data/raw/3112026uksponsor.csv", newline = "") as sponsor:
    content = csv.DictReader(sponsor)
    headername = content.fieldnames
    sponsorlist = list(content)
    countrow = len(sponsorlist)
    town_counts = {}
    sorted_town_counts = []
    for row in sponsorlist:
        town = row['Town/City']
        strippedtown = town.strip() #data cleaning to remove space
        lowertown = strippedtown.lower() #data cleaning
        town_counts[lowertown] = town_counts.get(lowertown, 0) + 1
    
    sorted_town_counts = sorted(town_counts.items(), key=lambda x: x[1], reverse=True)
    print(headername)
    print(countrow)
    print(sorted_town_counts[:10])

