from json import load
path="C:\\Users\\hp\\Desktop\\pythonworks\\decision_making\\read_fromjson\\movies\\mdb.json"
with open(path)as f:
  movies=load(f) 

# #   print total movies
# print(len(movies))

# # print all movies_name
# movies_name=[m.get("title")for m in movies]
# print(movies_name)

# movies_r=[m.get("title")for m in movies if m.get("year")=="2005"]
# print(movies_r)

# print movies titles whose geners="comedy"

# movies_geners=[m.get("title")for m in movies if "Comedy" in m.get("genres")]
# print(movies_geners)


# lengthy movie title

# l_movies=max(movies,key=lambda d:int(d.get("runtime")))
# print(l_movies)

# print all geners

# genres={g for m in movies for g in m.get("genres")}
# print(genres)

# comedy movies  released in 2015
# comedy_movies=[m.get("title") for m in movies if "Comedy" in m.get("genres") and m.get("year")=="2015" ]
# print(comedy_movies)

wc={}
for m in movies:
  year=m.get("year")
  if year in wc:
    wc[year]+=1
  else:
    wc[year]=1
print(wc)