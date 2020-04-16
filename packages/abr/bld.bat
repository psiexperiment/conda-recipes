set MENU_DIR=%PREFIX%\Menu
IF NOT EXIST (%MENU_DIR%) mkdir %MENU_DIR%

copy %RECIPE_DIR%\abr.ico %MENU_DIR%
if errorlevel 1 exit 1

copy %RECIPE_DIR%\menu-windows.json %MENU_DIR%\abr.json
if errorlevel 1 exit 1

%PYTHON% -m pip install . --no-deps
if errorlevel 1 exit 1
rd /s /q %SCRIPTS%
