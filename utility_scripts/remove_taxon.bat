@echo off
cd C:\Users\u7151703\Desktop\research\datasets\processing
for %%f in (*.txt) do (
    findstr /V "Leptolyngbya.PCC6306 Klebsormidium.SAG51.86" "%%f" > "%%f.temp"
    move /Y "%%f.temp" "%%f"
)
