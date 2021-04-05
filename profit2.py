import requests
bz = "https://api.hypixel.net/skyblock/bazaar?key=3f2bbc59-8b57-4534-bfaa-197800987801"
bzd = requests.get(bz).json()

for item in bzd['products']:
    try:
        if(bzd['products'][item]['quick_status']['buyPrice']*160<bzd['products'][f'ENCHANTED_{item}']['quick_status']['sellPrice']):
            print(f"{item} has an insta sell to insta buy difference of {bzd['products'][f'ENCHANTED_{item}']['quick_status']['sellPrice']-bzd['products'][item]['quick_status']['buyPrice']*160}")
    except KeyError:
        pass
