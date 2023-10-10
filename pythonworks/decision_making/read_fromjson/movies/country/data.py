from json import load
path="C:\\Users\\hp\\Desktop\\pythonworks\\decision_making\\read_fromjson\\movies\\country\\countries.json"
with open(path,encoding="utf-8")as f:
    countries=load(f)

# # total no:of countries
# print(len(countries))

# # print all country names
# all_countries=[c.get("name") for c in countries]
# print(all_countries)

# # print population below 10k country names
# l_population=[c.get("name") for c in countries if c.get("population")<=400000]
# print(l_population)


# # region=Asia
# country_region=[c.get("name") for c in countries if c.get("region")=="Asia"]
# print(country_region)



# language=[c.get("name") for c in countries for l in c.get("languages") if l.get("name")=="English"]
# print(language)

# starts_withc=[c.get("name")for c in countries if c.get("name").startswith("C")]
# print(starts_withc)
# # ------or------
# starts_withc=[c.get("name")for c in countries if c.get("name").casefold().startswith("c")]
# print(starts_withc)

# # border_sharing=[for c in countries]

# name_capital=[[c.get("name"),c.get("capital")]for c in countries]
# print(name_capital)

# c_with_borders=[c for c in countries if "borders" in c]
# max_border=max(c_with_borders,key=lambda c:len(c.get("borders")))
# print(max_border.get("name"))

# # border sharing with india
# india_borders=[c.get("borders")for c in countries if c.get("name")=="India"]#[]
# print(india_borders)

# india_borders=[c.get("borders")for c in countries if c.get("name")=="India"][0]#[]
# india_border_names=[c.get("name")for c in countries if c.get("alpha3Code") in india_borders]
# print(india_border_names)


# # print all regions
# all_regions={c.get("region")for c in countries}
# print(all_regions)

# dependent=[c.get("name")for c in countries if c.get("independent")]
# print(dependent)

##region_with country
wc={}
for c in countries:
  region=c.get("region")
  if region in wc:
    wc[region]+=1
  else:
    wc[region]=1
print(wc)

