fav_place = {'jeba': ['japan', 'canada', 'ukbekstan'], 'soikot': ['japan', 'england', 'hungrey'], 'david': ['pakistan', 'india', 'china']}
for name, places in fav_place.items():
    print(f"{name.title()}'s favorite places are:")
    for place in places:
        print(f"\t{place.title()}")
