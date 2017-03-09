# Hodor Mobile App

This is the official Hodor app (currently just available for android)

## Dist version

In order to generate a debug mode apk, run `npm run apk:debug`. To run a release apk, you need to sign it first. The apk file will be generated at `android\app\build\outputs\apk\app-debug.apk`.

A temporal keystore file is required to enable deploying a release version. In order to do it, just run `npm run apk:release` and it will both generate a release apk at `android\app\build\outputs\apk\app-release.apk` and will set it up on your connected device.

For generating a keystore file, run `keytool -genkey -v -keystore mykeystore.keystore -alias mykeyalias -keyalg RSA -keysize 2048 -validity 10000`, then move it to `./android/app` and finally update the `./android/gradle.properties` file accordingly.

## FAQ

* How to change apk installation title ?
  renaming string `app_name` filed in `android/app/src/main/res/values/strings.xml` file

* How to change apk icons?
  upload icons in png format to `android/app/src/main/red/mipmap-xyz` folders
