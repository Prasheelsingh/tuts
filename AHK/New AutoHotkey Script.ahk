::joe::
Send, My First Script
return

::btw::
MsgBox, You typed btw.
return

::Esc::
MsgBox, Escape!!!!
return

^j::
MsgBox, Wow!
MsgBox, There are
Run, notepad.exe
WinActivate, Untitled - Notepad
WinWaitActive, Untitled - Notepad
Send, 7 lines{!}{Enter}
SendInput, inside the CTRL{+}J hotkey.
return

Numpad0 & Numpad1::
MsgBox, You pressed Numpad1 while holding down Numpad0.
return

Numpad0 & Numpad2::
Run, notepad.exe
return

; Untitled - Notepad
#IfWinActive Untitled - Notepad
!q::
MsgBox, You pressed ALT+Q in Notepad.
return

; Any window that isn't Untitled - Notepad
;#IfWinActive
;!q::
;MsgBox, You pressed ALT+Q in any window.
;return

#IfWinActive * - Notepad
!q::
MsgBox, You pressed ALT+Q on any Notepad.
return

; Notepad
#IfWinActive ahk_class Notepad
#Space::
MsgBox, You pressed WIN+SPACE in Notepad.
return
::msg::You typed msg in Notepad

; Completes the phrase with 'JACK'
~j::
Send, ack
return

; MSPaint
#IfWinActive Untitled - Paint
#Space::
MsgBox, You pressed WIN+SPACE in MSPaint!
return
::msg::You typed msg in MSPaint!

; Fires up without an ending character
:*:acheiv::achiev        
; Fires up only with an ending character
::achievment::achievement
::acquaintence::acquaintance
:*:adquir::acquir
::aquisition::acquisition

:*:agravat::aggravat

:*:allign::align

::ameria::America