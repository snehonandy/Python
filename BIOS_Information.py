import win32com.client
import wmi

connection = wmi.connect_server(server="", user="", password="")
c = wmi.WMI(wmi=connection)

objWMIService = win32com.client.Dispatch("WbemScripting.SWbemLocator")
objSWbemServices = objWMIService.ConnectServer(strComputer,"root\cimv2")
colItems = objSWbemServices.ExecQuery("Select * from Win32_BIOS")
for objItem in colItems:
    z = objItem.BiosCharacteristics
    if z is None:
        a = 1
    else:
        for x in z:
            print("Bios Characteristics: ", x)
    z = objItem.BIOSVersion
    if z is None:
        a = 1
    else:
        for x in z:
            print("BIOS Version: ", x)
    print("BIOS Version: ", objItem.BIOSVersion)
    print("Build Number: ", objItem.BuildNumber)
    print("Caption: ", objItem.Caption)
    print("Code Set: ", objItem.CodeSet)
    print("Current Language: ", objItem.CurrentLanguage)
    print("Description: ", objItem.Description)
    print("Identification Code: ", objItem.IdentificationCode)
    print("Installable Languages: ", objItem.InstallableLanguages)
    print("Install Date: ", objItem.InstallDate)
    print("Language Edition: ", objItem.LanguageEdition)
    z = objItem.ListOfLanguages
    if z is None:
        a = 1
    else:
        for x in z:
            print("List Of Languages: ", x)
    print("List Of Languages: ", objItem.ListOfLanguages)
    print("Manufacturer: ", objItem.Manufacturer)
    print("Name: ", objItem.Name)
    print("Other Target OS: ", objItem.OtherTargetOS)
    print("Primary BIOS: ", objItem.PrimaryBIOS)
    print("Release Date: ", objItem.ReleaseDate)
    print("Serial Number: ", objItem.SerialNumber)
    print("SMBIOS BIOS Version: ", objItem.SMBIOSBIOSVersion)
    print("SMBIOS Major Version: ", objItem.SMBIOSMajorVersion)
    print("SMBIOS Minor Version: ", objItem.SMBIOSMinorVersion)
    print("SMBIOS Present: ", objItem.SMBIOSPresent)
    print("Software Element ID: ", objItem.SoftwareElementID)
    print("Software Element State: ", objItem.SoftwareElementState)
    print("Status: ", objItem.Status)
    print("Target Operating System: ", objItem.TargetOperatingSystem)
    print("Version: ", objItem.Version)