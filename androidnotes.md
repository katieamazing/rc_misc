Android notes:

how to recompile:

delete the subfolder Android/android
go out into C:\Android
start the venv ( $ venv\Scripts\activate)
venv $ python setup.py android --class-name="MainActivity"
venv $ cd .\android
venv $ ./gradlew build installDebug
