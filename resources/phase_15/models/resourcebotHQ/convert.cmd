SetLocal EnableDelayedExpansion

for %%f in (*.egg) do (

    set file=%%f
    set str=!file:~0,-4!
    
    C:\Panda3D-1.11.0-x64-happie_fa\bin\egg2bam.exe %%f !str!.bam
)
pause