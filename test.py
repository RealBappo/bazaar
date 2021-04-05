import requests
import json
import os

bz = "https://api.hypixel.net/skyblock/bazaar?key=3f2bbc59-8b57-4534-bfaa-197800987801"
bd = requests.get(bz)
bzd = bd.json()
data = input("pick one, mining, farming, combat, wood, fish(this is case sensitive, no caps) :\n")
if bzd['success'] is True:
    if data == 'farming':           #farming
        farm = ({'wt' : f"{bzd['products']['WHEAT']['quick_status']}" ,
        'ebr' : f"{bzd['products']['ENCHANTED_BREAD']['quick_status']}" ,
        'hb' : f"{bzd['products']['HAY_BLOCK']['quick_status']}" ,
        'ehb' : f"{bzd['products']['ENCHANTED_HAY_BLOCK']['quick_status']}" ,
        'tphb' : f"{bzd['products']['TIGHTLY_TIED_HAY_BALE']['quick_status']}" ,
        'ct' : f"{bzd['products']['CARROT_ITEM']['quick_status']}" , 'ect' : 
        f"{bzd['products']['ENCHANTED_CARROT']['quick_status']}" , 'ects' : 
        f"{bzd['products']['ENCHANTED_CARROT_ON_A_STICK']['quick_status']}" , 'egct' : 
        f"{bzd['products']['ENCHANTED_GOLDEN_CARROT']['quick_status']}" , 'pt' : 
        f"{bzd['products']['POTATO_ITEM']['quick_status']}" , 'ept' : 
        f"{bzd['products']['ENCHANTED_POTATO']['quick_status']}" , 'ebpt' : 
        f"{bzd['products']['ENCHANTED_CARROT']['quick_status']}" , 'pk' : 
        f"{bzd['products']['PUMPKIN']['quick_status']}" , 'epk' : 
        f"{bzd['products']['ENCHANTED_PUMPKIN']['quick_status']}" , 'ppk' : 
        f"{bzd['products']['POLISHED_PUMPKIN']['quick_status']}" , 'mn' : 
        f"{bzd['products']['MELON']['quick_status']}" , 'emn' : 
        f"{bzd['products']['ENCHANTED_MELON']['quick_status']}" , 'emnb' : 
        f"{bzd['products']['ENCHANTED_MELON_BLOCK']['quick_status']}" , 'egmn' : 
        f"{bzd['products']['ENCHANTED_GLISTERING_MELON']['quick_status']}" , 'sd' : 
        f"{bzd['products']['SEEDS']['quick_status']}" , 'esd' : 
        f"{bzd['products']['ENCHANTED_SEEDS']['quick_status']}" , 'rmr' : 
        f"{bzd['products']['RED_MUSHROOM']['quick_status']}" , 'rmrb' : 
        f"{bzd['products']['HUGE_MUSHROOM_1']['quick_status']}" , 'ermr' : 
        f"{bzd['products']['ENCHANTED_RED_MUSHROOM']['quick_status']}" , 'ermrb' : 
        f"{bzd['products']['ENCHANTED_HUGE_MUSHROOM_1']['quick_status']}" , 'bmr' : 
        f"{bzd['products']['BROWN_MUSHROOM']['quick_status']}" , 'bmrb' : 
        f"{bzd['products']['HUGE_MUSHROOM_2']['quick_status']}" , 'ebmr' : 
        f"{bzd['products']['ENCHANTED_BROWN_MUSHROOM']['quick_status']}" , 'ebmrb' : 
        f"{bzd['products']['ENCHANTED_HUGE_MUSHROOM_2']['quick_status']}" , 'cc' : 
        f"{bzd['products']['INK_SACK:3']['quick_status']}" , 'ecc' : 
        f"{bzd['products']['ENCHANTED_COCOA']['quick_status']}" , 'ecke' : 
        f"{bzd['products']['ENCHANTED_COOKIE']['quick_status']}" , 'cs' : 
        f"{bzd['products']['CACTUS']['quick_status']}" , 'ecsg' : 
        f"{bzd['products']['ENCHANTED_CACTUS_GREEN']['quick_status']}" , 'ecs' : 
        f"{bzd['products']['ENCHANTED_CACTUS']['quick_status']}" , 'sc' : 
        f"{bzd['products']['SUGAR_CANE']['quick_status']}" , 'esg' : 
        f"{bzd['products']['ENCHANTED_SUGAR']['quick_status']}" , 'esp' : 
        f"{bzd['products']['ENCHANTED_PAPER']['quick_status']}" , 'esc' : 
        f"{bzd['products']['ENCHANTED_SUGAR_CANE']['quick_status']}" , 'fr' : 
        f"{bzd['products']['FEATHER']['quick_status']}" , 'efr' : 
        f"{bzd['products']['ENCHANTED_FEATHER']['quick_status']}" , 'lt' : 
        f"{bzd['products']['LEATHER']['quick_status']}" , 'elt' : 
        f"{bzd['products']['ENCHANTED_LEATHER']['quick_status']}" , 'bf' : 
        f"{bzd['products']['RAW_BEEF']['quick_status']}" , 'ebf' : 
        f"{bzd['products']['ENCHANTED_RAW_BEEF']['quick_status']}" , 'pc' : 
        f"{bzd['products']['PORK']['quick_status']}" , 'epc' : 
        f"{bzd['products']['ENCHANTED_PORK']['quick_status']}" , 'ecpc' : 
        f"{bzd['products']['ENCHANTED_GRILLED_PORK']['quick_status']}" , 'cn' : 
        f"{bzd['products']['RAW_CHICKEN']['quick_status']}" , 'ecn' : 
        f"{bzd['products']['ENCHANTED_RAW_CHICKEN']['quick_status']}" , 'eg' : f"{bzd['products']['ENCHANTED_EGG']['quick_status']}" , 'eck' : f"{bzd['products']['ENCHANTED_CAKE']['quick_status']}" , 'eeg
                 ' : f"{bzd['products']['SUPER_EGG']['quick_status']}" , 'mt' : f"{bzd['products']['MUTTON']['quick_status']}" , 'emt' : f"{bzd['products']['ENCHANTED_MUTTON']['quick_status']}" , 'ecmt' : f"{bzd['products']['ENCHANTED_COOKED_MUTTON']['quick_status']}" , 'rt' : f"{bzd['products']['RABBIT']['quick_status']}" , 'ert' : f"{bzd['products']['ENCHANTED_RABBIT']['quick_status']}" , 'rf' : f"{bzd['products']['RABBIT_FOOT']['quick_status']}" , 'rh' : f"{bzd['products']['RABBIT_HIDE']['quick_status']}" , 'erf' : f"{bzd['products']['ENCHANTED_RABBIT_FOOT']['quick_status']}" , 'erh' : f"{bzd['products']['ENCHANTED_RABBIT_HIDE']['quick_status']}" , 'nw' : f"{bzd['products']['NETHER_STALK']['quick_status']}" , 'enw' : f"{bzd['products']['ENCHANTED_NETHER_STALK']['quick_status']}" , 'mnw' : f"{bzd['products']['MUTANT_NETHER_STALK']['quick_status']}"})
        for item in farm:
            try:
                if farm[item]['buyPrice']*160<farm[f'e{item}']['sellPrice']:
                    print(f"{farm[f'{item}']['productId']} has an insta buy to insta sell difference of {farm[f'e{item}']['sellPrice']-farm[f'{item}']['buyPrice']*160}")
                elif farm['item']['buyPrice']*160>=farm[f'e{item}']['sellPrice']:
                    print('FUCK' + farm[f'{item}']['productId'])
            except KeyError:
                pass
json.load(123)      #i just have this so it keeps all the variables open
