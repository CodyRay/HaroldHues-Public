If WScript.Arguments.length =0 Then
  Set objShell = CreateObject("Shell.Application")
  'Pass a bogus argument with leading blank space, say [ uac]
  objShell.ShellExecute "wscript.exe", Chr(34) & _
  WScript.ScriptFullName & Chr(34) & " uac", "", "runas", 1
Else
Set Shell  = CreateObject("WScript.Shell")
'CurDir = Shell.CurrentDirectory & "\"
Shell.RUN chr(34) & "\\hsd.local\software\Repo\Deployment\Rhinoceros 5\Install.bat" & chr(34), 0, True
End If