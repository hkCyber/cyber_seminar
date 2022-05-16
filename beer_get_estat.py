#beer_get_e-stat_data.py

#このファイルで実行し得たデータを以下のURLへ格納しCyber大学のアカウントに対して共有しております
#https://drive.google.com/file/d/10jW5n0V9LljLHa2FVQ_0Eo2RIIRDwJoB/view?usp=sharing

import os
import pandas as pd
import csv
from csv import DictWriter

import beer_temp_config as conf

'''
下記URLからエクセルファイルを/%Y/%-mの形式で格納し以下を実行
https://www.e-stat.go.jp/stat-search/files?page=1&layout=datalist&toukei=00200561&tstat=000000330001&cycle=1&tclass1=000000330001&tclass2=000000330004&tclass3=000000330005&tclass4val=0
なぜか12.01.1のような形で数値が入る場合があったため、手動で修正しました。


To Do：
エクセルのダウンロードと格納は手動で行いましたが、
e-Statからの取得はSeleniumなどでエクセルをダウンロードするようにできると良いと思っています。
'''
#うるう年
leap_year = [2008, 2012, 2016]

#各月の日数
days_of_month = {
    1: 31,
    2: 28,
    3: 31,
    4: 30,
    5: 31,
    6: 30,
    7: 31,
    8: 31,
    9: 30,
    10: 31,
    11: 30,
    12: 31
}

#日数毎のe-Statから取得する日別支出の取得すべきエクセルのカラム範囲
column_range = {
    31: "K:AO",
    30: "K:AN",
    29: "K:AM",
    28: "K:AL"
}

#年毎のビールの消費支出の行
beer_row = {
    2006: 246,
    2007: 246,
    2008: 246,
    2009: 246,
    2010: 246,
    2011: 246,
    2012: 246,
    2013: 246,
    2014: 246,
    2015: 248,
    2016: 248
}

#取得時間の範囲定義
start_year = 2006
end_year = 2016
start_month = 1
end_month = 12

def insert_csv(year, month, data):
    headersCSV = ['年', '月', '日', 'ビール消費支出']

    for index, beer_expense in enumerate(data):
        dict={'年':year,'月':month,'日':index+1, 'ビール消費支出':beer_expense}

        with open(conf.csv_filepath_for_beer_expenses, 'a', newline='') as f:
            file_is_empty = os.stat(conf.csv_filepath_for_beer_expenses).st_size == 0
            if file_is_empty:
                csv.writer(f, lineterminator='\n').writerow(headersCSV)
            dictwriter_object = DictWriter(f, fieldnames=headersCSV)
            dictwriter_object.writerow(dict)
            f.close()

for year in range(start_year, end_year+1):
    for month in range(start_month, end_month+1):
        if ((year == 2008 or year == 2012 or year == 2016) and month == 2):
            df = pd.read_excel(conf.excel_filepath_for_beer_expenses_from_estat.format(year, month), sheet_name=0, skiprows=beer_row.get(year)-1, nrows=0, usecols=column_range.get(29))
            insert_csv(year, month, df.columns)
        else:
            df = pd.read_excel(conf.excel_filepath_for_beer_expenses_from_estat.format(year, month), sheet_name=0, skiprows=beer_row.get(year)-1, nrows=0, usecols=column_range.get(days_of_month.get(month)))
            insert_csv(year, month, df.columns)
