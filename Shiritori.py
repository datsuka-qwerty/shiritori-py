# coding: utf-8
from cgi import print_arguments
from operator import contains
import sys
from encodings import search_function


def main():
	# --set up--
	youon_dic = {"ァ": "ア", "ィ": "イ", "ゥ": "ウ", "ェ": "エ", "ォ": "オ","ッ": "ツ","ャ": "ヤ", "ュ": "ユ", "ョ": "ヨ", "ー": None} # 拗音・長音 変換用
	youon_table = str.maketrans(youon_dic) # 変換用テーブル作成

	used = ["シリトリ"]
	# --ends here--

	# --first time game--

	user_in = input("Input start wtih リ in カタカナ. ->")
	if user_in in used: # 既に使用済みの単語を入力された場合
		print(user_in+" is already used...")
		print("YOU LOSE!!! \n I WIN!!!!!!!")
		sys.exit()
	elif user_in[-1] == "ン": # ンで終わる単語の場合
		print("OH.... YOU ENTERED ン.... \n YOU LOSE!!! \n I WIN!!!!!!!")
		sys.exit()
	elif user_in[0] != "リ": # リで始まっていない場合、ゲーム開始時のみプログラム強制終了
		print(user_in+" is not starting with リ... \n Please retry :-)")
		sys.exit()
	else:
		pass

	used.append(user_in.replace("\n", ""))
	print("You entered "+user_in, end=" ")
	user_in_tr = user_in.translate(youon_table) # 拗音で終わる場合、translateで変換
	print("and the last letter is "+user_in_tr[-1])

	dic = open("./Dic/"+user_in_tr[-1]+".txt", "r", encoding="utf-8") # dicへ対応する文字のtxtを開く

	cnt = 0 # 探索中の行を読み取るカウンタリセット

	if cnt == len(dic.readlines()): # もし、txtの中身がからの場合
		print("Oh no...... \n I have no idea... \n Congratulations!!! YOU WIN!!!")
		sys.exit()
	else:
		pass

	dic = open("./Dic/"+user_in_tr[-1]+".txt", "r", encoding="utf-8") # dicへ対応する文字のtxtを開く

	# 回答用の単語を探していく
	for searching_string in dic.readlines():
		cnt = cnt + 1
		if cnt == len(dic.readlines()): # 回答出来なかった場合ー＞ファイルの一番最後まで探索しても回答単語が見つからなかった場合
			print("Oh no...... \n I have no idea... \n Congratulations!!! YOU WIN!!!")
			sys.exit()
		elif searching_string.replace("\n", "") not in used:
			tmp = searching_string
			used.append(searching_string.replace("\n", ""))
			break

	print("Well.... I'll say "+tmp) # 回答
	# --ends here--

	# --loop game--
	while(1):
		tmp = tmp.replace("\n", "") # txtに含まれる改行コード削除
		tmp_tr = tmp.translate(youon_table) # 拗音・長音 変換
		user_in = input("Input start with "+tmp_tr[-1]+" in カタカナ. ->") # 入力要求

		if user_in in used: # 使用済みリストにいる場合
			print(user_in+" is already used...")
			print("YOU LOSE!!! \n I WIN!!!!!!!")
			sys.exit()
		elif user_in[-1] == "ン": # ンで終わってる場合
			print("OH.... YOU ENTERED ン.... \n YOU LOSE!!! \n I WIN!!!!!!!")
			sys.exit()
		elif user_in[0] != tmp_tr[-1]: # ルールを満たしていない場合
			print(user_in+" is not starting with "+tmp_tr[-1]+"... \n Please retry :-)")
			continue # whileの先頭へ戻る
		else:
			pass

		used.append(user_in.replace("\n", ""))
		print("You entered "+user_in, end=" ")
		user_in_tr = user_in.translate(youon_table) # 拗音で終わる場合、translateで変換
		print("and the last letter is "+user_in_tr[-1])

		dic = open("./Dic/"+user_in_tr[-1]+".txt", "r", encoding="utf-8") # 対応する文字のtxtファイルを開く

		cnt = 0

		if cnt == len(dic.readlines()):
			print("Oh no...... \n I have no idea... \n Congratulations!!! YOU WIN!!!")
			sys.exit()
		else:
			pass

		dic = open("./Dic/"+user_in_tr[-1]+".txt", "r", encoding="utf-8") # dicへ対応する文字のtxtを開く

		for searching_string in dic.readlines():
			cnt = cnt + 1
			print("fuck search "+searching_string.replace("\n", ""))
			if cnt == len(dic.readlines()):
				print("Oh no...... \n I have no idea... \n Congratulations!!! YOU WIN!!!")
				sys.exit()
			elif searching_string.replace("\n", "") not in used:
				tmp = searching_string
				used.append(searching_string.replace("\n", ""))
				break

		print("Well.... I'll say "+tmp)
		continue
	# --ends here--


if __name__ == "__main__":
	main()