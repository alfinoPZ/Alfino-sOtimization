import colorama
from colorama import Fore, Style
import time
import os
import subprocess
import getpass

colorama.init()

print(Fore.RED + "!!!WARNING!!!" + Style.RESET_ALL)
print(Fore.RED + "YOU CAN USE YOUR KEY JUST ONCE. SO THE 2 KEYS THAT YOU RECEIVED CAN ONLY BE USED ONCE" + Style.RESET_ALL)
time.sleep(7)
os.system("cls")

serial_keys = [
    'dtqv1g-cw22mu-asd123',
    'a2dv12-dsau12-as11d1',
    'jnn2aa-sad221-1vv1ab',
    'a2gasd-dasb11-asd1vv'
]

# Diretório do usuário
user_directory = os.path.expanduser("~")

# Pasta "Local" dentro do diretório "AppData" do usuário
local_appdata_folder = os.path.join(user_directory, "AppData", "Local")

# Pasta para armazenar as chaves utilizadas
data_folder = os.path.join(local_appdata_folder, "AlfinoPZCleaner")

# Verificar se a pasta de dados existe
if not os.path.exists(data_folder):
    # Cria a pasta se não existir
    os.makedirs(data_folder)

# Arquivo para armazenar as chaves utilizadas
used_keys_file = os.path.join(data_folder, "used_keys.txt")

# Verificar se o arquivo de chaves usadas já existe
if not os.path.exists(used_keys_file):
    # Cria o arquivo se não existir
    open(used_keys_file, "w").close()

# Ler as chaves já utilizadas a partir do arquivo
with open(used_keys_file, "r") as file:
    used_keys = file.read().splitlines()

def asduadvbzjkhadvbzdjad():
    while True:
        print(Fore.YELLOW + f"MADE BY: " + Style.RESET_ALL + f"")
        time.sleep(1.5)

        print(Fore.WHITE + f"""
                ░█████╗░██╗░░░░░███████╗██╗███╗░░██╗░█████╗░██████╗░███████╗
                ██╔══██╗██║░░░░░██╔════╝██║████╗░██║██╔══██╗██╔══██╗╚════██║
                ███████║██║░░░░░█████╗░░██║██╔██╗██║██║░░██║██████╔╝░░███╔═╝
                ██╔══██║██║░░░░░██╔══╝░░██║██║╚████║██║░░██║██╔═══╝░██╔══╝░░
                ██║░░██║███████╗██║░░░░░██║██║░╚███║╚█████╔╝██║░░░░░███████╗
                ╚═╝░░╚═╝╚══════╝╚═╝░░░░░╚═╝╚═╝░░╚══╝░╚════╝░╚═╝░░░░░╚══════╝
        """ + Style.RESET_ALL) # https://fsymbols.com/generators/carty/

        time.sleep(3.3)
        print("Select an option: ")
        print("1 " + Fore.YELLOW +f"- [+] Clean all my computer" + Style.RESET_ALL)
        time.sleep(1)
        print("2 " + Fore.YELLOW +f"- [+] Decrease inputLag + Better fps" + Style.RESET_ALL)
        time.sleep(1)
        print("3 " + Fore.YELLOW +f"- [+] Better Apps for your Windows" + Style.RESET_ALL)
        time.sleep(1)
        print("4 " + Fore.YELLOW +f"- [+] Clean FiveM" + Style.RESET_ALL)
        time.sleep(1)
        print("5 " + Fore.YELLOW +f"- [+] Logout FiveM account" + Style.RESET_ALL)
        time.sleep(1)
        print("6 " + Fore.YELLOW +f"- [+] Exit" + Style.RESET_ALL)
        answer = int(input("> "))

        answer_1 = "Clean all my computer"
        answer_2 = "Decrease inputLag + Better fps"
        answer_3 = "Better Apps for your Windows"
        answer_4 = "Clean FiveM"
        answer_5 = "Logout FiveM account"

        match answer:
            case 1:
                print("Option choosen: " + Fore.YELLOW + f"{answer_1}" + Style.RESET_ALL)
                print(Fore.RED + "Removing:\n- Temporary files\n- Log files\n- Update cache files\n- Windows event log\n- Program uninstall files" + Style.RESET_ALL)
                subprocess.run('@echo off & takeown /f "%temp%" /r /d y', shell=True, creationflags=subprocess.CREATE_NO_WINDOW)
                subprocess.run('@echo off & RD /S /Q %temp%', shell=True, creationflags=subprocess.CREATE_NO_WINDOW)
                subprocess.run('@echo off & MKDIR %temp%', shell=True, creationflags=subprocess.CREATE_NO_WINDOW)
                subprocess.run('@echo off &takeown /f "%temp%" /r /d y', shell=True, creationflags=subprocess.CREATE_NO_WINDOW)
                subprocess.run('@echo off &takeown /f "C:\Windows\Temp" /r /d y', shell=True, creationflags=subprocess.CREATE_NO_WINDOW)
                subprocess.run('@echo off &RD /S /Q C:\Windows\Temp', shell=True, creationflags=subprocess.CREATE_NO_WINDOW)
                subprocess.run('@echo off & MKDIR C:\Windows\Temp', shell=True, creationflags=subprocess.CREATE_NO_WINDOW)
                subprocess.run('@echo off & takeown /f "C:\Windows\Temp" /r /d y', shell=True, creationflags=subprocess.CREATE_NO_WINDOW)
                
                subprocess.run('@echo off & cd C:/ & del *.log /a /s /q /f', shell=True, creationflags=subprocess.CREATE_NO_WINDOW)
                
                subprocess.run('@echo off & net stop wuauserv', shell=True, creationflags=subprocess.CREATE_NO_WINDOW)
                subprocess.run('@echo off &net stop UsoSvc', shell=True, creationflags=subprocess.CREATE_NO_WINDOW)
                subprocess.run('@echo off & rd /s /q C:\Windows\SoftwareDistribution', shell=True, creationflags=subprocess.CREATE_NO_WINDOW)
                subprocess.run('@echo off &md C:\Windows\SoftwareDistribution', shell=True, creationflags=subprocess.CREATE_NO_WINDOW)
                
                subprocess.run('@echo off & FOR %F IN ("%SystemRoot%\servicing\Packages\Microsoft-Windows-GroupPolicy-ClientTools-Package~*.mum") DO (DISM /Online /NoRestart /Add-Package:"%F")', shell=True, creationflags=subprocess.CREATE_NO_WINDOW)
                subprocess.run('@echo off & FOR %F IN ("%SystemRoot%\servicing\Packages\Microsoft-Windows-GroupPolicy-ClientExtensions-Package~*.mum") DO (DISM /Online /NoRestart /Add-Package:"%F")', shell=True, creationflags=subprocess.CREATE_NO_WINDOW)
                
                subprocess.run('@echo off &wevtutil cl Security', shell=True, creationflags=subprocess.CREATE_NO_WINDOW)
                subprocess.run('@echo off & wevtutil cl System', shell=True, creationflags=subprocess.CREATE_NO_WINDOW)
                subprocess.run('@echo off &wevtutil cl Application', shell=True, creationflags=subprocess.CREATE_NO_WINDOW)
                
                subprocess.run('@echo off &rd /s /q "C:\Program Files\*.msi"', shell=True, creationflags=subprocess.CREATE_NO_WINDOW)

                time.sleep(0.7)
                print("\n" + Fore.GREEN + f"Files REMOVED" + Style.RESET_ALL)
                time.sleep(1)
                print("Wait...")
                time.sleep(5)
                subprocess.run("cls", shell=True)

            case 2:
                def create_system_restore_point(description):
                    command = f'wmic.exe /Namespace:\\\\root\\default Path SystemRestore Call CreateRestorePoint "{description}", 100, 7'
                    subprocess.run(command, shell=True, creationflags=subprocess.CREATE_NO_WINDOW)

                # Exemplo de uso
                description = "Ponto de restauração criado pelo Cleaner - AlfinoPZ"
                create_system_restore_point(description)

                print(f"Option choosen: " + Fore.YELLOW + f"{answer_2}")
                print(Fore.RED + "Decreasing InputLag..." + Style.RESET_ALL)
                print(Fore.RED + "WARNING: A RestorePoint has already been created!")

                NetAdapterBinding = 'Enable-NetAdapterBinding -Name "*" -ComponentID ms_pacer'  # Comando do PowerShell
                result = subprocess.run(['powershell', NetAdapterBinding], capture_output=True, text=True)

                time.sleep(5)

                GameConfigStore = 'Set-ItemProperty -Path "HKCU:\\System\\GameConfigStore" -Name "GameDVR_Enabled" -Value 0 -Type DWord'  
                result = subprocess.run(['powershell', GameConfigStore], capture_output=True, text=True)
                if result.returncode == 0:
                    print(Fore.GREEN + "Sucessfully" + Style.RESET_ALL)
                else:
                    print(Fore.RED + "Error GameConfigStore" + Style.RESET_ALL)

                time.sleep(5)

                AllowGameDVR = 'Set-ItemProperty -Path "HKLM:\\SOFTWARE\\Microsoft\\PolicyManager\\default\\ApplicationManagement\\AllowGameDVR" -Name "value" -Value 0 -Type DWord'
                result = subprocess.run(['powershell', AllowGameDVR], capture_output=True, text=True)
                if result.returncode == 0:
                    print(Fore.GREEN + "Sucessfully" + Style.RESET_ALL)
                else:
                    print(Fore.RED + "Error AllowGameDVR" + Style.RESET_ALL)

                time.sleep(5)

                GameDVR = 'Set-ItemProperty -Path "HKLM:\\SOFTWARE\\Policies\\Microsoft\\Windows\\GameDVR" -Name "AllowGameDVR" -Value 0 -Type DWord'
                result = subprocess.run(['powershell', GameDVR], capture_output=True, text=True)
                if result.returncode == 0:
                    print(Fore.GREEN + "Sucessfully" + Style.RESET_ALL)
                else:
                    print(Fore.RED + "Error GameDVR" + Style.RESET_ALL)

                time.sleep(5)

                AppCaptureEnabled = 'Set-ItemProperty -Path "HKCU:\\SOFTWARE\\Microsoft\\Windows\\CurrentVersion\\GameDVR" -Name "AppCaptureEnabled" -Value 0 -Type DWord'
                result = subprocess.run(['powershell', AppCaptureEnabled], capture_output=True, text=True)
                if result.returncode == 0:
                    print(Fore.GREEN + "Sucessfully" + Style.RESET_ALL)
                else:
                    print(Fore.RED + "Error AppCaptureEnabled" + Style.RESET_ALL)
    
                time.sleep(5)

                PowerThrottlingOff = 'Set-ItemProperty -Path "HKLM:\\SYSTEM\\CurrentControlSet\\Control\\Power\\PowerThrottling" -Name "PowerThrottlingOff" -Value 1 -Type DWord'
                result = subprocess.run(['powershell', PowerThrottlingOff], capture_output=True, text=True)
                if result.returncode == 0:
                    print(Fore.GREEN + "Sucessfully" + Style.RESET_ALL)
                else:
                    print(Fore.RED + "Error PowerThrottlingOff" + Style.RESET_ALL)
                time.sleep(5)

                EnableLUA = 'Set-ItemProperty -Path "HKLM:\\SOFTWARE\\Microsoft\\Windows\\CurrentVersion\\Policies\\System" -Name "EnableLUA" -Value 0 -Type DWord'
                result = subprocess.run(['powershell', EnableLUA], capture_output=True, text=True)
                if result.returncode == 0:
                    print(Fore.GREEN + "Sucessfully" + Style.RESET_ALL)
                else:
                    print(Fore.RED + "Error EnableLUA" + Style.RESET_ALL)

                time.sleep(5)

                FeatureSettingsOverride = 'Set-ItemProperty -Path "HKLM:\\SYSTEM\\CurrentControlSet\\Control\\Session Manager\\Memory Management" -Name "FeatureSettingsOverride" -Value 3 -Type DWord'
                FeatureSettingsOverrideMask = 'Set-ItemProperty -Path "HKLM:\\SYSTEM\\CurrentControlSet\\Control\\Session Manager\\Memory Management" -Name "FeatureSettingsOverrideMask" -Value 3 -Type DWord'

                result1 = subprocess.run(['powershell', FeatureSettingsOverride], capture_output=True, text=True)
                result2 = subprocess.run(['powershell', FeatureSettingsOverrideMask], capture_output=True, text=True)

                if result1.returncode == 0 and result2.returncode == 0:
                    print(Fore.GREEN + "Sucessfully" + Style.RESET_ALL)
                else:
                    print(Fore.RED + "Error FeatureSettingsOverride and FeatureSettingsOverrideMask" + Style.RESET_ALL)

                time.sleep(5)

                EnableTransparency = 'Set-ItemProperty -Path "HKCU:\\SOFTWARE\\Microsoft\\Windows\\CurrentVersion\\Themes\\Personalize" -Name "EnableTransparency" -Value 0 -Type DWord'
                result = subprocess.run(['powershell', EnableTransparency], capture_output=True, text=True)
                if result.returncode == 0:
                    print(Fore.GREEN + "Sucessfully" + Style.RESET_ALL)
                else:
                    print(Fore.RED + "Error EnableTransparency" + Style.RESET_ALL)

                time.sleep(5)

                os.system("""
                        @echo off
                        cls.
                        @echo off
                        PowerShell "Disable-MMAgent -MemoryCompression"
                        """)
                
                time.sleep(5)

                defender = input(Fore.RED + "Disable WindowsDefender? (y/n) " + Style.RESET_ALL)
                if defender.lower() == "y":
                    windowsDefender = [
                        'Set-ItemProperty -Path "HKLM:\\SYSTEM\\CurrentControlSet\\Services\\wdboot" -Name "Start" -Value 4 -Type DWord',
                        'Set-ItemProperty -Path "HKLM:\\SYSTEM\\CurrentControlSet\\Services\\wdfilter" -Name "Start" -Value 4 -Type DWord',
                        'Set-ItemProperty -Path "HKLM:\\SYSTEM\\CurrentControlSet\\Services\\WinDefend" -Name "Start" -Value 4 -Type DWord',
                        'Set-ItemProperty -Path "HKLM:\\SYSTEM\\CurrentControlSet\\Services\\SecurityHealthService" -Name "Start" -Value 4 -Type DWord',
                        'Set-ItemProperty -Path "HKLM:\\SYSTEM\\CurrentControlSet\\Services\\wdnisdrv" -Name "Start" -Value 4 -Type DWord',
                        'Set-ItemProperty -Path "HKLM:\\SYSTEM\\CurrentControlSet\\Services\\mssecflt" -Name "Start" -Value 4 -Type DWord',
                        'Set-ItemProperty -Path "HKLM:\\SYSTEM\\CurrentControlSet\\Services\\WdNisSvc" -Name "Start" -Value 4 -Type DWord',
                        'Set-ItemProperty -Path "HKLM:\\SYSTEM\\CurrentControlSet\\Services\\Sense" -Name "Start" -Value 4 -Type DWord',
                        'Set-ItemProperty -Path "HKLM:\\SYSTEM\\CurrentControlSet\\Services\\wscsvc" -Name "Start" -Value 4 -Type DWord',
                        'Set-ItemProperty -Path "HKLM:\\SOFTWARE\\Policies\\Microsoft\\Windows Defender" -Name "DisableAntiSpyware" -Value 1 -Type DWord',
                        'Set-ItemProperty -Path "HKLM:\\SOFTWARE\\Policies\\Microsoft\\Windows Defender" -Name "DisableRoutinelyTakingAction" -Value 1 -Type DWord',
                        'Set-ItemProperty -Path "HKLM:\\SOFTWARE\\Policies\\Microsoft\\Windows Defender" -Name "ServiceKeepAlive" -Value 0 -Type DWord',
                        'Set-ItemProperty -Path "HKLM:\\SOFTWARE\\Policies\\Microsoft\\Windows Defender\\Real-Time Protection" -Name "DisableBehaviorMonitoring" -Value 1 -Type DWord',
                        'Set-ItemProperty -Path "HKLM:\\SOFTWARE\\Policies\\Microsoft\\Windows Defender\\Real-Time Protection" -Name "DisableIOAVProtection" -Value 1 -Type DWord',
                        'Set-ItemProperty -Path "HKLM:\\SOFTWARE\\Policies\\Microsoft\\Windows Defender\\Real-Time Protection" -Name "DisableOnAccessProtection" -Value 1 -Type DWord',
                        'Set-ItemProperty -Path "HKLM:\\SOFTWARE\\Policies\\Microsoft\\Windows Defender\\Real-Time Protection" -Name "DisableRealtimeMonitoring" -Value 1 -Type DWord',
                        'Set-ItemProperty -Path "HKLM:\\SOFTWARE\\Policies\\Microsoft\\Windows Defender\\Reporting" -Name "DisableEnhancedNotifications" -Value 1 -Type DWord',
                        'Set-ItemProperty -Path "HKLM:\\SOFTWARE\\Policies\\Microsoft\\Windows Defender Security Center\\Notifications" -Name "DisableNotifications" -Value 1 -Type DWord',
                        'Set-ItemProperty -Path "HKCU:\\Software\\Policies\\Microsoft\\Windows\\CurrentVersion\\PushNotifications" -Name "NoToastApplicationNotification" -Value 1 -Type DWord',
                        'Set-ItemProperty -Path "HKCU:\\Software\\Policies\\Microsoft\\Windows\\CurrentVersion\\PushNotifications" -Name "NoToastApplicationNotificationOnLockScreen" -Value 1 -Type DWord'
                    ]

                    for command in windowsDefender:
                        result = subprocess.run(['powershell', command], capture_output=True, text=True)
                        if result.returncode == 0:
                            print(Fore.GREEN + "Sucessfully" + Style.RESET_ALL)
                        else:
                            print(Fore.RED + "Error (windowsDefender)" + Style.RESET_ALL)
                    time.sleep(1)
                elif defender.lower() == "n":
                    pass
                else:
                    pass

                time.sleep(5)

                os.system(""""
                        @echo off
                        cls.
                        @echo off
                        bcdedit /set disabledynamictick yes
                        bcdedit /deletevalue useplatformclock
                        bcdedit /set useplatformtick yes        
                        """)
                
                time.sleep(5)

                registry = [
                    'Set-ItemProperty -Path "HKLM:\\SYSTEM\\CurrentControlSet\\Control\\Power\\PowerThrottling" -Name "PowerThrottlingOff" -Value 1 -Type DWord',
                    'Set-ItemProperty -Path "HKLM:\\SOFTWARE\\Microsoft\\Windows NT\\CurrentVersion\\Multimedia\\SystemProfile" -Name "NetworkThrottlingIndex" -Value 10 -Type DWord',
                    'Set-ItemProperty -Path "HKLM:\\SOFTWARE\\Microsoft\\Windows NT\\CurrentVersion\\Multimedia\\SystemProfile" -Name "SystemResponsiveness" -Value 0 -Type DWord',
                    'Set-ItemProperty -Path "HKLM:\\SOFTWARE\\Microsoft\\Windows NT\\CurrentVersion\\Multimedia\\SystemProfile\\Tasks\\Games" -Name "Affinity" -Value 0 -Type DWord',
                    'Set-ItemProperty -Path "HKLM:\\SOFTWARE\\Microsoft\\Windows NT\\CurrentVersion\\Multimedia\\SystemProfile\\Tasks\\Games" -Name "Background Only" -Value "False" -Type String',
                    'Set-ItemProperty -Path "HKLM:\\SOFTWARE\\Microsoft\\Windows NT\\CurrentVersion\\Multimedia\\SystemProfile\\Tasks\\Games" -Name "Clock Rate" -Value 10000 -Type DWord',
                    'Set-ItemProperty -Path "HKLM:\\SOFTWARE\\Microsoft\\Windows NT\\CurrentVersion\\Multimedia\\SystemProfile\\Tasks\\Games" -Name "GPU Priority" -Value 8 -Type DWord',
                    'Set-ItemProperty -Path "HKLM:\\SOFTWARE\\Microsoft\\Windows NT\\CurrentVersion\\Multimedia\\SystemProfile\\Tasks\\Games" -Name "Priority" -Value 6 -Type DWord',
                    'Set-ItemProperty -Path "HKLM:\\SOFTWARE\\Microsoft\\Windows NT\\CurrentVersion\\Multimedia\\SystemProfile\\Tasks\\Games" -Name "Scheduling Category" -Value "High" -Type String',
                    'Set-ItemProperty -Path "HKLM:\\SOFTWARE\\Microsoft\\Windows NT\\CurrentVersion\\Multimedia\\SystemProfile\\Tasks\\Games" -Name "SFIO Priority" -Value "High" -Type String',
                    'Set-ItemProperty -Path "HKCU:\\System\\GameConfigStore" -Name "GameDVR_Enabled" -Value 0 -Type DWord',
                    'Set-ItemProperty -Path "HKCU:\\System\\GameConfigStore" -Name "GameDVR_FSEBehaviorMode" -Value 2 -Type DWord',
                    'Set-ItemProperty -Path "HKCU:\\System\\GameConfigStore" -Name "GameDVR_HonorUserFSEBehaviorMode" -Value 0 -Type DWord',
                    'Set-ItemProperty -Path "HKCU:\\System\\GameConfigStore" -Name "GameDVR_DXGIHonorFSEWindowsCompatible" -Value 1 -Type DWord',
                    'Set-ItemProperty -Path "HKCU:\\System\\GameConfigStore" -Name "GameDVR_EFSEFeatureFlags" -Value 0 -Type DWord',
                    'Set-ItemProperty -Path "HKCU:\\Control Panel\\Desktop" -Name "AutoEndTasks" -Value "1" -Type String',
                    'Set-ItemProperty -Path "HKCU:\\Control Panel\\Desktop" -Name "HungAppTimeout" -Value "1000" -Type String',
                    'Set-ItemProperty -Path "HKCU:\\Control Panel\\Desktop" -Name "WaitToKillAppTimeout" -Value "2000" -Type String',
                    'Set-ItemProperty -Path "HKCU:\\Control Panel\\Desktop" -Name "LowLevelHooksTimeout" -Value "1000" -Type String',
                    'Set-ItemProperty -Path "HKCU:\\Control Panel\\Desktop" -Name "MenuShowDelay" -Value "0" -Type String',
                    'Set-ItemProperty -Path "HKLM:\\SYSTEM\\CurrentControlSet\\Control" -Name "WaitToKillServiceTimeout" -Value "2000" -Type String',
                    'Set-ItemProperty -Path "HKLM:\\SOFTWARE\\Microsoft\\Windows NT\\CurrentVersion\\Schedule\\Maintenance" -Name "MaintenanceDisabled" -Value 1 -Type DWord',
                    'Set-ItemProperty -Path "HKLM:\\SYSTEM\\CurrentControlSet\\Control\\Power" -Name "HibernateEnabled" -Value 0 -Type DWord'
                ]

                for command in registry:
                    result = subprocess.run(['powershell', command], capture_output=True, text=True)
                    if result.returncode == 0:
                        print(Fore.GREEN + "Sucessfully" + Style.RESET_ALL)
                    else:
                        print(Fore.RED + "Error Registry" + Style.RESET_ALL)

                time.sleep(5)

                mouse = input(Fore.RED + "Fix mouse Problem? (ONLY WINDOWS 10) (y/n) " + Style.RESET_ALL)
                if mouse.lower() == "y":
                    print(Fore.GREEN + "[+] MouseFixed+" + Style.RESET_ALL)
                    mousefix = [
                    'REG ADD "HKEY_CURRENT_USER\Control Panel\Mouse" /v "MouseSensitivity" /t REG_SZ /d "10" /f',
                    'REG ADD "HKEY_CURRENT_USER\Control Panel\Mouse" /v "SmoothMouseXCurve" /t REG_BINARY /d "0000000000000000C0CC0C00000000008099190000000040662600000000333300000000" /f',
                    'REG ADD "HKEY_CURRENT_USER\Control Panel\Mouse" /v "SmoothMouseYCurve" /t REG_BINARY /d "0000000000000000003800000000000070000000000000A800000000000000E00000000000" /f',
                    'REG ADD "HKEY_USERS\.DEFAULT\Control Panel\Mouse" /v "MouseSpeed" /t REG_SZ /d "0" /f',
                    'REG ADD "HKEY_USERS\.DEFAULT\Control Panel\Mouse" /v "MouseThreshold1" /t REG_SZ /d "0" /f',
                    'REG ADD "HKEY_USERS\.DEFAULT\Control Panel\Mouse" /v "MouseThreshold2" /t REG_SZ /d "0" /f'
                    ]
                    # Executa cada comando do registro
                    for command in mousefix:
                        result = subprocess.run(command, capture_output=True, text=True, shell=True)
                        if result.returncode == 0:
                            print(Fore.GREEN + "Sucessfully" + Style.RESET_ALL)
                        else:
                            print(Fore.RED + "Error MouseFix" + Style.RESET_ALL)
                    time.sleep(1)
                elif mouse.lower() == "n":
                    pass
                else:
                    pass

                time.sleep(5)

                services1 = [
                'REG ADD "HKEY_LOCAL_MACHINE\SYSTEM\CurrentControlSet\Services\DiagTrack" /v "Start" /t REG_DWORD /d "4" /f',
                'REG ADD "HKEY_LOCAL_MACHINE\SYSTEM\CurrentControlSet\Services\dmwappushservice" /v "Start" /t REG_DWORD /d "4" /f',
                'REG ADD "HKEY_LOCAL_MACHINE\SYSTEM\CurrentControlSet\Services\diagsvc" /v "Start" /t REG_DWORD /d "4" /f',
                'REG ADD "HKEY_LOCAL_MACHINE\SYSTEM\CurrentControlSet\Services\DPS" /v "Start" /t REG_DWORD /d "4" /f',
                'REG ADD "HKEY_LOCAL_MACHINE\SYSTEM\CurrentControlSet\Services\diagnosticshub.standardcollector.service" /v "Start" /t REG_DWORD /d "4" /f',
                'REG ADD "HKEY_LOCAL_MACHINE\SYSTEM\CurrentControlSet\Services\WdiServiceHost" /v "Start" /t REG_DWORD /d "4" /f',
                'REG ADD "HKEY_LOCAL_MACHINE\SYSTEM\CurrentControlSet\Services\WdiSystemHost" /v "Start" /t REG_DWORD /d "4" /f'
                ]

                # Executa cada comando do registro
                for command in services1:
                    result = subprocess.run(command, capture_output=True, text=True, shell=True)
                    if result.returncode == 0:
                        print(Fore.GREEN + "Sucessfully" + Style.RESET_ALL)
                    else:
                        print(Fore.RED + "Error Services1" + Style.RESET_ALL)

                time.sleep(5)

                services2 = [
                'REG ADD "HKEY_LOCAL_MACHINE\SYSTEM\CurrentControlSet\Services\WbioSrvc" /v "Start" /t REG_DWORD /d "4" /f',
                'REG ADD "HKEY_LOCAL_MACHINE\SYSTEM\CurrentControlSet\Services\FontCache" /v "Start" /t REG_DWORD /d "4" /f',
                'REG ADD "HKEY_LOCAL_MACHINE\SYSTEM\CurrentControlSet\Services\FontCache3.0.0.0" /v "Start" /t REG_DWORD /d "4" /f',
                'REG ADD "HKEY_LOCAL_MACHINE\SYSTEM\CurrentControlSet\Services\GraphicsPerfSvc" /v "Start" /t REG_DWORD /d "4" /f',
                'REG ADD "HKEY_LOCAL_MACHINE\SYSTEM\CurrentControlSet\Services\stisvc" /v "Start" /t REG_DWORD /d "4" /f',
                'REG ADD "HKEY_LOCAL_MACHINE\SYSTEM\CurrentControlSet\Services\WerSvc" /v "Start" /t REG_DWORD /d "4" /f',
                'REG ADD "HKEY_LOCAL_MACHINE\SYSTEM\CurrentControlSet\Services\PcaSvc" /v "Start" /t REG_DWORD /d "4" /f',
                'REG ADD "HKEY_LOCAL_MACHINE\SYSTEM\CurrentControlSet\Services\Wecsvc" /v "Start" /t REG_DWORD /d "4" /f'
                ]

                # Executa cada comando do registro
                for command in services2:
                    result = subprocess.run(command, capture_output=True, text=True, shell=True)
                    if result.returncode == 0:
                        print(Fore.GREEN + "Sucessfully" + Style.RESET_ALL)
                    else:
                        print(Fore.RED + "Error services2" + Style.RESET_ALL)

                time.sleep(5)

                xbox = input(Fore.RED + "Disable Xbox's servies? (y/n) " + Style.RESET_ALL)
                if xbox.lower() == "y":
                    print(Fore.GREEN + "[+] Xbox Services+" + Style.RESET_ALL)
                    
                    xbox_services = [
                    'REG ADD "HKEY_LOCAL_MACHINE\SYSTEM\CurrentControlSet\Services\MapsBroker" /v "Start" /t REG_DWORD /d "4" /f',
                    'REG ADD "HKEY_LOCAL_MACHINE\SYSTEM\CurrentControlSet\Services\Spooler" /v "Start" /t REG_DWORD /d "4" /f',
                    'REG ADD "HKEY_LOCAL_MACHINE\SYSTEM\CurrentControlSet\Services\PrintNotify" /v "Start" /t REG_DWORD /d "4" /f'
                    ]

                    # Executa cada comando do registro
                    for command in xbox_services:
                        result = subprocess.run(command, capture_output=True, text=True, shell=True)
                        if result.returncode == 0:
                            print(Fore.GREEN + "Sucessfully." + Style.RESET_ALL)
                        else:
                            print(Fore.RED + "Error Xbox Services" + Style.RESET_ALL)

                    time.sleep(1)
                elif xbox.lower() == "n":
                    pass
                else:
                    pass
                
                print(Fore.GREEN + f"InputLag decreased" + Style.RESET_ALL)
                time.sleep(1)
                print("Wait... Your PC will be restarted")
                time.sleep(5)
                os.system("cls")
                os.system("shutdown /r /t 1")

            case 3:
                print(f"Option choosen: " + Fore.YELLOW + f"{answer_3}" + Style.RESET_ALL)
                time.sleep(1)
                cleanmgr = input(Fore.RED + "Install Cleanmgr+? (y/n) " + Style.RESET_ALL)
                if cleanmgr.lower() == "y":
                    print(Fore.GREEN + "[+] Cleanmgr+" + Style.RESET_ALL)
                    os.system("start https://cdn.discordapp.com/attachments/1083214209174737008/1126759123694932048/cleanmgr-1-38-1200.zip")
                    time.sleep(1)
                elif cleanmgr.lower() == "n":
                    pass
                else:
                    pass
                
                autoruns = input(Fore.RED + "Install Autoruns? (y/n) " + Style.RESET_ALL)
                if autoruns.lower() == "y":
                    print(Fore.GREEN + "[+] Autoruns" + Style.RESET_ALL)
                    os.system("start https://download.sysinternals.com/files/Autoruns.zip")
                    time.sleep(1)
                elif autoruns.lower() == "n":
                    pass
                else:
                    pass
                
                memoryCleaner = input(Fore.RED + "Install Memory Cleaner? (y/n) " + Style.RESET_ALL)
                if memoryCleaner.lower() == "y":
                    print(Fore.GREEN + "[+] Memory Cleaner" + Style.RESET_ALL)
                    os.system("start https://cdn.discordapp.com/attachments/1083214209174737008/1126761653569069186/memorycleaner.exe")
                    time.sleep(1)
                elif memoryCleaner.lower() == "n":
                    pass
                else:
                    pass

                msiMode = input(Fore.RED + "Install MSI Mode Utility? (y/n) " + Style.RESET_ALL)
                if msiMode.lower() == "y":
                    print(Fore.GREEN + "[+] MSI Mode Utility" + Style.RESET_ALL)
                    os.system("start https://cdn.discordapp.com/attachments/1083214209174737008/1126761801573470208/MSI_util_v3.exe")
                    time.sleep(1)
                elif msiMode.lower() == "n":
                    pass
                else:
                    pass

                ddu = input(Fore.RED + "Install Display Driver Uninstaller (DDU)? (y/n) " + Style.RESET_ALL)
                if ddu.lower() == "y":
                    print(Fore.GREEN + "[+] Display Driver Uninstaller (DDU)" + Style.RESET_ALL)
                    os.system("start https://cdn.discordapp.com/attachments/1083214209174737008/1126762245490217010/Guru3D.com-DDU.zip")
                elif ddu.lower() == "n":
                    pass
                else:
                    pass

                profile = input(Fore.RED + "Install Nvidia Profile Inspector? (y/n) " + Style.RESET_ALL)
                if profile.lower() == "y":
                    print(Fore.GREEN + "[+] Nvidia Profile Inspector (DDU)" + Style.RESET_ALL)
                    os.system("start https://cdn.discordapp.com/attachments/1083214209174737008/1126766122188939405/nvidiaProfileInspector.exe")
                elif profile.lower() == "n":
                    pass
                else:
                    pass

                tcp = input(Fore.RED + "Install TCP View? (y/n) " + Style.RESET_ALL)
                if tcp.lower() == "y":
                    print(Fore.GREEN + "[+] TCP View" + Style.RESET_ALL)
                    os.system("start https://cdn.discordapp.com/attachments/1083214209174737008/1126766724046409778/TCPView.exe")
                elif tcp.lower() == "n":
                    pass
                else:
                    pass

                explorer = input(Fore.RED + "Install Process Explorer? (y/n) " + Style.RESET_ALL)
                if explorer.lower() == "y":
                    print(Fore.GREEN + "[+] Process Explorer" + Style.RESET_ALL)
                    os.system("start https://cdn.discordapp.com/attachments/1083214209174737008/1126767247944335410/Process_Explorer.exe")
                elif explorer.lower() == "n":
                    pass
                else:
                    pass

                network = input(Fore.RED + "Install NetworkLatencyView? (y/n) " + Style.RESET_ALL)
                if network.lower() == "y":
                    print(Fore.GREEN + "[+] NetworkLatencyView" + Style.RESET_ALL)
                    os.system("start https://cdn.discordapp.com/attachments/1083214209174737008/1126768848096477285/NetworkLatencyView.rar")
                elif network.lower() == "n":
                    pass
                else:
                    pass
            
                time.sleep(1)
                print("Wait...")
                time.sleep(5)
                os.system("cls")
            
            case 4:
                print(f"Option chosen: " + Fore.YELLOW + f"{answer_4}" + Style.RESET_ALL)
                time.sleep(1)
                print(Fore.RED + "Removing logs" + Style.RESET_ALL)
                subprocess.run(r'@echo off & cls. & @echo off & set "pasta=C:\Users\%USERNAME%\AppData\Local\FiveM\FiveM.app\logs" & for %%F in ("%pasta%\*.*") do (del /q "%%F")', shell=True, creationflags=subprocess.CREATE_NO_WINDOW)
                print(Fore.GREEN + "Logs removed" + Style.RESET_ALL)
                time.sleep(5)

                print(Fore.RED + "Removing data" + Style.RESET_ALL)
                subprocess.run(r'@echo off & cls. & @echo off & set "pasta=C:\Users\%USERNAME%\AppData\Local\FiveM\FiveM.app\data" & set "subpasta=game-storage" & if not exist "%pasta%" mkdir "%pasta%" & for /D %%I in ("%pasta%\*") do (if /I not "%%~nxI"=="%subpasta%" (del /q "%%I\*.*" & rd /s /q "%%I" > nul 2>&1))', shell=True, creationflags=subprocess.CREATE_NO_WINDOW)
                print(Fore.GREEN + "Data removed" + Style.RESET_ALL)
                time.sleep(5)

                print(Fore.RED + "Removing crashes" + Style.RESET_ALL)
                subprocess.run(r'@echo off & cls. & @echo off & set "pasta=C:\Users\%USERNAME%\AppData\Local\FiveM\FiveM.app\crashes" & for /F "delims=" %%F in (\'dir /B /A:-D "%pasta%\*"\') do (del /q "%pasta%\%%F")', shell=True, creationflags=subprocess.CREATE_NO_WINDOW)
                print(Fore.GREEN + "Crashes removed" + Style.RESET_ALL)

                time.sleep(1)
                print("Wait...")
                time.sleep(5)
                subprocess.run("cls", shell=True, creationflags=subprocess.CREATE_NO_WINDOW)
                time.sleep(1)
                print("Wait...")
                time.sleep(5)
                os.system("cls")

            case 5:
                print(f"Option chosen: " + Fore.YELLOW + f"{answer_5}" + Style.RESET_ALL)
                time.sleep(1)
                print(Fore.RED + "Loggin out")

                subprocess.run(r'@echo off & set "folder=C:\Users\alfinopz\AppData\Local\DigitalEntitlements" & if exist "%folder%" (rmdir /s /q "%folder%") else (echo The folder DigitalEntitlements does not exist.)', shell=True, creationflags=subprocess.CREATE_NO_WINDOW)

                print(Fore.GREEN + "LOGGED OUT" + Style.RESET_ALL)
                time.sleep(1)
                print("Wait...")
                time.sleep(5)
                os.system("cls")
            case 6:
                exit(0)

serial_key_input = input(Fore.RED + "First of all. Entry a valid serial key: " + Style.RESET_ALL)

if serial_key_input in serial_keys:
    if serial_key_input in used_keys:
        print(Fore.YELLOW + "This key has already been used. Please enter a valid key." + Style.RESET_ALL)
        time.sleep(3)
        exit(0)
    else:
        print(Fore.GREEN + "KEY VALID" + Style.RESET_ALL)
        used_keys.append(serial_key_input)  # Adiciona a chave utilizada à lista de chaves usadas

        # Atualizar o arquivo de chaves usadas
        with open(used_keys_file, "a") as file:
            file.write(serial_key_input + "\n")

        time.sleep(2.5)
        os.system("cls")
        asduadvbzjkhadvbzdjad()
else:
    print(Fore.RED + "KEY NOT VALID" + Style.RESET_ALL)
    time.sleep(3)
    exit(0)
