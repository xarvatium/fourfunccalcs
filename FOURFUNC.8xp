// Yes, this is a calculator meant to run inside of a calculator... I got bored one day in math class.

:" A FOUR FUNCTION CALCULATOR IN TI-BASIC
:Lbl A
:Disp "INPUT OPERATOR"
:Input "(+, -, *, /): ",X
:" STOPS IF INPUT IS 0
:If X=0:Then
::Stop
:End
:
:Input "FIRST NUM: ",A
:Input "SECOND NUM: ",B
:
:If X=1:Then
::Disp A+B
:Else
:
:If X=2:Then
::Disp A-B
:Else
:
:If X=4:Then
::Disp A/B
:End
:End
:End
:Goto A