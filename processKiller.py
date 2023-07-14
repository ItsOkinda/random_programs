import platform
import os
import wmi
import psutil


# GET OS TYPE FIRST

systems = platform.release()
print(systems)
def killer():
    if systems == 'Windows':

        k = wmi.WMI()
        print (" processID       ProcessName")
        for process in k.Win32_Process():
            
            # Displaying the P_ID and P_Name of the process
            print(f"{process.ProcessId:<10} {process.Name}")
            # adjust the code to kill all running processes 
            # enjoy
            if process.name =='AnyDesk.exe':
                process.Terminate()
            else:
                print("Process not found")

    else:
        # this code for linux works on all platforms apparently
        
        print("processName           ProcessId")
        m=0
        for process in psutil.process_iter():
            
            print(f"{process.name()}      {process.pid}")

            m=m+1
        print(f"no of processes are {m}")

            #process.kill()
            # run the command within the loop to crash a system and kill all running processes



