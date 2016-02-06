@echo off
(
"\\hsd.local\software\Repo\Deployment\Rhinoceros 5\DotNet\dotNetFx40_Full_setup.exe" /q /norestart
ping -n 100 127.0.0.1
msiexec /i "\\hsd.local\software\Repo\Deployment\Rhinoceros 5\Extracted Files\Installers\rhino5setup_en-us_x86.msi" /qb INSTALLDIR="C:\Program Files (x86)\Rhinoceros 5" RMA_CDKEY=J8G25400T09J3V98QQ2A INSTALL_EN=1 
ping -n 100 127.0.0.1
msiexec /i "\\hsd.local\software\Repo\Deployment\Rhinoceros 5\Extracted Files\Installers\LanguagePack_en-us.msi" /qn
ping -n 100 127.0.0.1
msiexec /i "\\hsd.local\software\Repo\Deployment\Rhinoceros 5\Extracted Files\Installers\HelpMedia.msi" /qn
)>NUL 2>NUL