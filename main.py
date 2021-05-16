import csv

#変数の呼び出し
from setting import FILE_PATH, NEW_FILE_PATH, GET_LINE
#関数の呼び出し
from change_height import change


with open(FILE_PATH, mode='r', encoding='utf-8') as file:
    reader = csv.reader(file)

    #最初の1行を飛ばす
    next(reader)


    csv_list = []

    #csv_listにGET_LINEで入力した数字分csvファイルの上から列を取得
    for row in reader:
        if len(csv_list) <= GET_LINE:
            csv_list.append(row)
        else:
            break
    

    with open(NEW_FILE_PATH, mode='w',newline='', encoding='utf-8') as new_file:
        writer = csv.writer(new_file)
        #一行目に入るタイトル的なやつ
        writer.writerow(["名前", "性別", "身長（2倍）"])

        for line in csv_list:

            #身長を任意の数字倍にする--------------------------------------------

            #名前が入っているカラム
            name_column = line[1]
            #性別が入っているカラム
            height_column = line[2]
            #身長が入っているカラム
            height_column = line[6]

            #元の身長に掛け算する数字
            change_num = 2

            #change_height.pyからchange関数を呼び出し引数に身長が入ってるカラムを入れる
            #第二引数には何倍にするかの数字（change_num）を入れる
            new_height = change(height_column, change_num)

            #名前と性別と倍にした身長を表示　他は割愛ーーーーーーーーーーーーーーーーーーー

            #身長データがマイナスなものはunknownと表示する
            if new_height < 0:
                writer.writerow([name_column,height_column,'unknown'])
            else:
                writer.writerow([name_column,height_column,int(new_height)])
            

