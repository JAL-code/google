import win32com.client

access = win32com.client.Dispatch("Access.Application")
access.DoCmd.OpenForm("Search for Scriptures Form")
