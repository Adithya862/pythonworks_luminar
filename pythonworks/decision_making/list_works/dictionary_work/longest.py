text="hello good hello goodmorning"
words=text.split(" ")
longest_word=max(words,key=lambda w:len(w))#w:oro wordum
print(longest_word)



text="hi hello good s hello goodmorning z"
words=text.split(" ")
longest_word=min(words,key=lambda w:len(w))
print(longest_word)

srt_word=sorted(words,key=lambda w:len(w),reverse=True)
print(srt_word)





