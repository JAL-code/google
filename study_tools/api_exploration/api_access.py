import win32com.client

access = win32com.client.Dispatch("Access.Application")

for item in dir(access.docmd):
    print(item)
