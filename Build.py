#!/usr/bin/env python3
import os
import unicodedata
from urllib.request import urlopen

Name = "twemoji-amazing"
EmojiVer = "15.0"

# https://stackoverflow.com/a/518232
def StripAccents(s):
	return ''.join(c for c in unicodedata.normalize('NFD', s)
		if unicodedata.category(c) != 'Mn')

#https://unpkg.com/emoji.json@13.1.0/emoji.json

def ReplaceList(Text, Match, Replace):
	for m in Match:
		Text = Text.replace(m, Replace)
	return Text

def CheckEmojiLine(Line):
	if Line.startswith("#"):
		return False
	if "; fully-qualified" not in Line:
		return False
	return True

def GetEmojiMeta(Line):
	Line = Line.lower()

	Code = Line.split(";")[0].rstrip(" ")
	Code = ReplaceList(Code, ["fe0f","200d"], "")
	Code = Code.replace("  ", " ")
	Code = ReplaceList(Code, [" ","--"], "-")
	Code = Code.removesuffix("-")

	Char = Line.split("# ")[1].split(" ")[0]

	Name = StripAccents("-".join(Line.split("# ")[1].split(" ")[2:]))
	Name = ReplaceList(Name, [":",".","&","(",")"], "")
	Name = Name.replace("--", "-").replace("--", "-") # Strange bug?

	return {"Code":Code, "Char":Char, "Name":Name}

def MinifyCSS(CSS):
	return ReplaceList(CSS, ["\n","\t"," "], "")

def Main():
	#print("[I] Cloning Twemoji repo")
	#os.system("git clone --depth 1 https://github.com/twitter/twemoji")

	print(f"[I] Getting v{EmojiVer} emoji data")
	Response = urlopen(f"https://unicode.org/Public/emoji/{EmojiVer}/emoji-test.txt")

	print("[I] Parsing emoji data")
	Emojis = []
	Data = Response.read().decode("utf-8")
	for Line in Data.splitlines():
		if CheckEmojiLine(Line):
			Emojis += [GetEmojiMeta(Line)]

	print(f"[I] Writing CSS")
	CSS = ""
	with open("Preamble.css", "r") as f:
		CSS += f.read()
	for Emoji in Emojis:
		CSS += f"""\
.twa-{Emoji["Name"]}, .twa-{Emoji["Char"]} {{
	background-image: url("{Emoji["Code"]}.svg");
}}
"""
	with open(f"{Name}.css", "w") as f:
		f.write(CSS)
	with open(f"{Name}.min.css", "w") as f:
		f.write(MinifyCSS(CSS))

if __name__ == "__main__":
	Main()
