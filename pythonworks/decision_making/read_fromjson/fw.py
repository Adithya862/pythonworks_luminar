from json import load
path="C:\\Users\\hp\\Desktop\\pythonworks\\decision_making\\read_fromjson\\data.json"
# open(path,mode,encoding="utf-8")
with open(path)as f:
    records=load(f)
# print(records)
# for f in records:
#     print(f.get("name"))

f_name=[f.get("name") for f in records]
print(f_name)
top_fw=max(records,key=lambda d:d.get("rating"))
print(top_fw)
# frontend fw names
# python fw names
