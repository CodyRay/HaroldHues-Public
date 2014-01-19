@echo off
mkdir "C:\Users\Public\Desktop\Data Files"
icacls "C:\Users\Public\Desktop\Data Files" /inheritance:r /grant:r "All Staff":(OI)(CI)F /grant:r "administrators":(OI)(CI)R /grant:r "SYSTEM":(OI)(CI)F /grant:r "administrator":(OI)(CI)F /grant:r "HSD\administrator":(OI)(CI)F /grant:r "administrator":(OI)(CI)F /grant:r "Domain Users":(OI)(CI)R
robocopy "\\hsd.local\student\HHS\Shared\Video Production\Public Desktop Win7 64bit\CS6" "C:\Public\Desktop\Data Files" /e

mkdir "C:\Data Files"
icacls "C:\Data Files" /inheritance:r /grant:r "administrators":(OI)(CI)R /grant:r "Domain Users":(OI)(CI)F /grant:r "SYSTEM":(OI)(CI)F
robocopy "\\hsd.local\student\HHS\Shared\Video Production\Public Desktop Win7 64bit\CS6" "C:\Data Files" /e

pause
