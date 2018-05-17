#NoEnv  ; Recommended for performance and compatibility with future AutoHotkey releases.
; #Warn  ; Enable warnings to assist with detecting common errors.
SendMode Input  ; Recommended for new scripts due to its superior speed and reliability.
SetWorkingDir %A_ScriptDir%  ; Ensures a consistent starting directory.

; Create the array, initially empty:
Array := [] ; or Array := Array()


Loop, Read, data.csv
{
    Array.Push(A_LoopReadLine) ; Append this line to the array.
}


