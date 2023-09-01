import os
import webbrowser
import pyautogui
import time
def Opening_Class():    
	time.sleep(20)    
	#Opening GOogle    
	os.startfile ("C:\\Users\\User\\PycharmProjects\\Class Starter\\Denver (greenvalleyschools.in) chrome.lnk")    
	time.sleep(4)    
	#Maximizing_Window    
	pyautogui.keyUp('win')   
	pyautogui.press('up')    
	pyautogui.keyDown('win')    
	#opening meet    
	webbrowser.open('https://meet.google.com')    
	time.sleep (5)    
	pyautogui.press('enter')        
	#Opening Classroom    
	time.sleep(5)    
	webbrowser.open('https://classroom.google.com/')
	Knowledge = input("Do You Have Class Today? \n")
	if Knowledge.lower() == "yes":    
		print ("Ok, Getting Ready...")    
		time.sleep(5)    
		Opening_Class()    
	else:    
		print("Ok, Have a GOOD time!")    
		time.sleep(5)    
	quit()

Opening_Class()
