call %ANDROID_NDK%\ndk-build -j 3

call ant debug
adb install -r bin\KlayGE_Tutor2-debug.apk