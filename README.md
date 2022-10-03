# mbot

Create env file for project
```
cd mbot_mqtt_movement
python3 -m venv env
source env/bin/activate
pip install -r requirements.txt
```

Copy unit file to systemd folder
```
sudo cp mbot_start.service /etc/systemd/system
```

Start unit file
```
sudo systemctl start mbot_start.service
```