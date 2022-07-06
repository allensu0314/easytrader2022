import easytrader

user = easytrader.use('universal_client')

user.prepare(exe_path=r"C:\同花顺远航版\bin\happ.exe")

print(user.balance)
