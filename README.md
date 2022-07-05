# deepl-pdf-trans
Using Python and selenium, press shotcut key and deepl to run the translation without line breaks.

# driver install
Please refer to the following URL for driver installation and configuration.
[driver install](https://www.selenium.dev/ja/documentation/webdriver/getting_started/install_drivers/)

# install
```console
git clone https://github.com/komo135/deepl-pdf-trans.git
cd deepl-pdf-trans

pip install -r requirements.txt
```

# run
![image.png](https://qiita-image-store.s3.ap-northeast-1.amazonaws.com/0/130763/22e75471-a56d-641f-0335-52ab279bb08a.png)

To translate into Japanese
```console
cd deepl-pdf-trans
python trans.py ja
```
To translate into English
```console
cd deepl-pdf-trans
python trans.py en
```

# put shortcut key
Press shortcut at the same time to execute the translation, then press esc to exit the program

![image](https://user-images.githubusercontent.com/66017773/161294250-d3407770-b221-4680-bdc9-cf5cdcda981a.png)

# error
If the shortcut key does not respond, please reload.
