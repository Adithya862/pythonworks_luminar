foods=[
    {"id":1,"name":"ghee-roast","price":70,"category":"veg"},
    {"id":2,"name":"chicken-roast","price":170,"category":"non-veg"},
    {"id":3,"name":"cb","price":170,"category":"non-veg"},
    {"id":4,"name":"bb","price":190,"category":"non-veg"},
    {"id":5,"name":"fried-rice","price":140,"category":"veg"},
    {"id":6,"name":"chicken-friedrice","price":170,"category":"non-veg"},
    {"id":7,"name":"nan","price":70,"category":"veg"},
    {"id":8,"name":"alfham","price":370,"category":"non-veg"},
     
]
# total number of items

# print(len(foods))
# # print name whose category = veg
# veg_items=[f.get("name") for f in foods if f.get("category")=="veg"]
# print(veg_items)
# # food names available under rs 100
# price_filter=[f.get("name")for f in foods if f.get("price")<=100]
# print(price_filter)
# # costly item
# costly_item=max(foods,key=lambda f:f.get("price"))
# print(costly_item)
# #costly non-veg food
# non_veg=[f for f in foods f.get("category")=="non-veg"]
# costly_nonveg=max(non_veg,key=lambda f:f.get("price"))
# print(costly_nonveg)

category={f.get("category") for f in foods}#duplication is not allowed-{}
print(category)
