First, install Docker.

```
sudo apt-get install docker.io
```

Then, download the dockerfile and run.

```
wget https://raw.githubusercontent.com/AStupidBear/skypecall/master/skypecall.Dockerfile.py
python skypecall.Dockerfile.py --user xxxx --passwd xxxx --callto xxxx
```

If you don't want to use docker, you can run the python file directly after setting up selenium and google-chrome manually.

```
pip install selenium
npm install -g selenium-side-runner
npm install -g chromedriver
wget https://dl.google.com/linux/direct/google-chrome-stable_current_amd64.deb
sudo apt install -y ./google-*.deb && rm google-*.deb
wget https://raw.githubusercontent.com/AStupidBear/skypecall/master/skypecall.py
python skypecall.py --user xxxx --passwd xxxx --callto xxxx
```
