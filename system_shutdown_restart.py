import os


def shutdown(self):
    os.chdir("C:\WINDOWS\system32")
    os.system("shutdown /s")


def restart(self):
    os.chdir("C:\WINDOWS\system32")
    os.system("shutdown /r")


def abort_shutdown(self):
    os.chdir("C:\WINDOWS\system32")
    os.system("shutdown /a")


def hibernate(self):
    os.chdir("C:\WINDOWS\system32")
    os.system("shutdown /h")
