import random;

last = 13
rnd = random.randint(0, last)

def main():
  print("Keep it logically awesome.")

  f = open("quotes.txt",encoding="utf-8") #寫 Python 做資料處理時讀取中文檔案有時候會遇到 UnicodeDecodeError: 'cp950' codec can't decode byte 0xe8 in position 7: illegal multibyte sequence 的錯誤，每次發生我都要重新找一次解決方法，一直記不住… 乾脆直接寫下來!
  quotes = f.readlines()
  f.close()

  print(quotes[rnd]) #print the first array 

if __name__== "__main__":
  main()
