import requests as r
import os
import json 
from time import sleep

def init():
    head = ("""
╭━━━┳╮╱╱╱╱╭━╮╭━╮
┃╭━╮┃┃╱╱╱╱┃┃╰╯┃┃
┃╰━━┫╰━┳━━┫╭╮╭╮┣━━╮
╰━━╮┃╭╮┃╭╮┃┃┃┃┃┃┃━┫
┃╰━╯┃┃┃┃╰╯┃┃┃┃┃┃┃━┫
╰━━━┻╯╰┻━━┻╯╰╯╰┻━━╯""")
    print(head)
    print("_____Developed by Vishnuxx_____\n")
    print("    (1) Quick Scan")
    print("    (2) Deep Scan")
    print("\n")
   
   
def scan(url , arr , deep):
    with open(".seclist.txt" , 'r') as fin:
        count = 0
        m_url = ""
        lines = fin.readlines()
        for line in lines:
            count = count + 1
            try:
                m_url = (f"{url} / {line}")
                response = r.get(m_url)
                if not response.status_code() == 404:
                    print(f"url: {m_url} \n status: {response.status_code()}")
                    obj = {"url" : m_url , "status" : response.status_code()}
                    arr.append(obj)
                    if deep:
                        scan(m_url , arr , deep)
            except Exception as e:
                               print(f"Exception Occured: {e}")
                               break


def save(lis):
    sv = input("Do you want to save as file?[y/n]")
    if sv == "y":
        filename = input("Save as filename : ")
        with open(filename , 'w' , encoding = 'utf-8') as f:
             json.dump(lis , f , ensure_ascii = False , indent = 4)
    elif sv == "n":
         cont = input("Do you want to continue this program?[y/n] : ")
         if cont == "y":
             main()
    else:
         cont = input("Do you want to continue this program?[y/n] : ")
         if cont == "y":
             main()       
                     
             
def main():
    os.system("clear")
    init()
    mode = input("Mode : ")
    inp = input("Enter root domain URL : ") 
    lis = []
    if mode == "1":
        print("Starting Quick Scan")
        scan(inp , lis , False)
        save(lis)
    elif mode == "2":
                print("Starting Deep Scan")
                scan(inp , lis , True)
                save(lis)
                                
main()
