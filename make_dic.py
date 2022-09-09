# coding: utf-8
import csv
from turtle import end_fill

def main():
	kana = open("./Gojuon.txt", "r", encoding="utf-8") # open A~Z file


	for goju in kana:
		print("Make new file "+goju.rstrip()+".txt in ./Dic/")
		tmp = open("./Dic/"+goju.rstrip()+".txt", "w", encoding="utf-8") # make A~Z .txt file
		f = open("./book.txt", "r", encoding="utf-8") # open BASED dictionary
		for line in f:
			if (line.startswith(goju.rstrip())) and ((line.rstrip()).endswith("ン") != True) and ((line.rstrip()).endswith("ー") != True): # search start with A~Z
				print(line, end="")
				print(line, end="", file=tmp) # writing to txt file
			else:
				pass
		tmp.close()
		f.close()

if __name__ == "__main__":
	main() # execute