
Note: Set all wires up before keeping reading. Negative jumper must go into 3rd pin right column and positive jumper into 4th pin left column (right and left looking ethernet port in pi in front of your eyes)

Upload this content into your pi:

if do not know how to access your pi, connect it to your local network and to your pc or power source and discover hosts with ssh enabled

```bash
$> nmap -p 22 -sV 192.168.1.0/24
```

Then try with default login/passwd:

```bash
# Enter with default settings
ssh pi@<IP> # i.e. ssh pi@192.168.1.135
# Use raspberry as passwd
```

Once got access into your pi, download this gist to your pi

```bash
git clone https://gist.github.com/9a77d698f05dbd11fb27c59ee172a48d.git garage_doors && cd garage_doors
```

Give permissions to setup if neede and run the script to install dependencies:

```bash
chmod +x ./scripts/setup.sh
./scripts/setup.sh
```

After that open a screen session:

```bash
screen -S garage_doors
# use <C-a-d> to come back to main shell and then from main shell use screen -r garage_doors
# to kill, type exit within screen session
```

To run the tests:

```bash
chmod +x ./scripts/tests.sh
./scripts/tests.sh
```

Finally run the process:

```bash
sudo python run.py
```

Note: for connectivity issues, make sure file /etc/network/interfaces is working (i.e `ping google.com`, or if firewall does not accept pinging, then use `curl --silent --head https://google.com`)
