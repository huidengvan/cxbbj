import pysrt
subs = pysrt.open("/Users/jzhang/git-repos/hdclass/vse/4/02-1 慧灯禅修课24 加行的修法-菩提心1.srt")

for sub in subs:
    print(sub.text)
    print()