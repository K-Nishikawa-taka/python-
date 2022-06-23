#メソッドとは処理の塊
#呼び出されるまで読み込まれない
def study(lang):
  print(f"{lang}入門")
  print(f"{lang}講座")
  
study("Python")
  
def ask():
  print("質問はコメント欄で")
  
def say_age(me="私", age=30):
  print(f"{me}は{age}才です")
  
ask()
say_age()
say_age("君")
say_age("君", 40)
