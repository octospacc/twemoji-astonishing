#!/usr/bin/env python3
import argparse
import os
import rcssmin
import unicodedata
from time import ctime
from pathlib import Path
from urllib.request import urlopen

cssmin = rcssmin._make_cssmin(python_only=True)

# https://stackoverflow.com/a/518232
def StripAccents(s):
	return ''.join(c for c in unicodedata.normalize('NFD', s)
		if unicodedata.category(c) != 'Mn')

def ReplaceList(Text, Match, Replace):
	for m in Match:
		Text = Text.replace(m, Replace)
	return Text

def GetEmojiData(EmojiVer):
	Response = urlopen(f"https://unicode.org/Public/emoji/{EmojiVer}/emoji-test.txt")
	return Response.read().decode("utf-8")

def ParseEmojiData(Data):
	Emojis = []
	for Line in Data.splitlines():
		if CheckEmojiLine(Line):
			Emojis += [GetEmojiMeta(Line)]
	return Emojis

def CheckEmojiLine(Line):
	if Line.startswith("#"):
		return False
	if "; fully-qualified" not in Line:
		return False
	return True

def GetEmojiMeta(Line):
	Line = Line.lower()

	Code = Line.split(";")[0].rstrip(" ")
	# Code = ReplaceList(Code, ["fe0f","200d"], "")
	Code = Code.replace("  ", " ")
	Code = ReplaceList(Code, [" ","--"], "-")
	Code = Code.removesuffix("-")

	Char = Line.split("# ")[1].split(" ")[0]

	Name = StripAccents("-".join(Line.split("# ")[1].split(" ")[2:]))
	Name = ReplaceList(Name, [":",".","&","(",")"], "")
	Name = Name.replace("--", "-").replace("--", "-") # Strange bug?

	return {"Code":Code, "Char":Char, "Name":Name}

def WriteCSS(Emojis, Output, URLPrefix):
	Path(Output).mkdir(parents=True, exist_ok=True)
	with open("Preamble.css", "r") as f:
		Preamble = f.read() + "\n"
	with open("Comment.css", "r") as f:
		Comment = f.read().format(BuildTime=ctime(), EmojiCount=str(len(Emojis)))

	for Type in ["Chars Names", "Chars", "Names"]:
		CSS = Preamble
		Line = ""
		if "Chars" in Type:
			Line = ".twa-{EmojiChar} " + Line
		if "Names" in Type:
			Line = ".twa-{EmojiName} " + Line
		if Type == "Chars Names":
			Line = Line.replace(" .twa-", ", .twa-")

		for Emoji in Emojis:
			NewLine = Line.format(EmojiChar=Emoji["Char"], EmojiName=Emoji["Name"])
			CSS += f"""\
{NewLine}{{
	background-image: url("{URLPrefix}{Emoji["Code"]}.svg");
}}
"""
		FileName = "twemoji-astonishing"
		if Type == "Chars":
			FileName += ".chars"
		elif Type == "Names":
			FileName += ".names"

		with open(f"{Output}{FileName}.css", "w") as f:
			f.write(CSS.replace("{CommentBlock}", Comment))
		with open(f"{Output}{FileName}.min.css", "w") as f:
			f.write(cssmin(CSS).replace("{CommentBlock}", "\n"+Comment))

def Main(Args):
	Output = Args.Output if Args.Output else "Build/"
	EmojiVer = Args.EmojiVer if Args.EmojiVer else "15.0"
	URLPrefix = Args.URLPrefix if Args.URLPrefix else "i/"

	print(f"[I] Getting v{EmojiVer} emoji data")
	Data = GetEmojiData(EmojiVer)

	print("[I] Parsing emoji data")
	Emojis = ParseEmojiData(Data)

	print(f"[I] Writing CSS to: {Output}")
	WriteCSS(Emojis, Output, URLPrefix)

if __name__ == "__main__":
	Parser = argparse.ArgumentParser()
	Parser.add_argument('--Output', type=str)
	Parser.add_argument('--EmojiVer', type=str)
	Parser.add_argument('--URLPrefix', type=str)

	Main(Parser.parse_args())
