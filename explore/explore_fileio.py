import csv

with open ("/home/bxbzwe/projects/SponsorMatch/data/raw/3112026uksponsor.csv", newline = "") as sponsor:
    #raw open
    # content = sponsor.readlines()
    # print(content[:5])
    #csv open
    # content = csv.reader(sponsor)
    # sponsorlist = list(content)
    # print(sponsorlist[:5])
    # dict open
    content = csv.DictReader(sponsor)
    sponsorlist = list(content)
    print(sponsorlist[:5])