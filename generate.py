import requests, json, random

f = open("./README.md", "w")
pokemon_id = random.randint(1, 151)
res = requests.get(f'https://pokeapi.co/api/v2/pokemon/{pokemon_id}')
result = json.loads(res.text)
f.write(f'''

<p align="center">
    <img src="{result['sprites']['front_default']}" width="150" height="150">
</p>
<h3 align="center">You have been greeted by a wild <b>{result['name'].title()}</b></h3>
<h3 align="center">Have a nice day!</h3>

# wireguard-go-builder

Compiling the [wireguard-go](https://git.zx2c4.com/wireguard-go/) binary from source. With this binary, users are able to create WireGuard sessions without installing the kernel module (if not preloaded for Linux Kernel 5.6 and above).

## Download

The latest version of the binary can be downloaded by clicking on the following link.



## Install

You can easily use a one-click script to automatically install to your Linux device:

```
curl -fsSL git.io/wireguard-go.sh | sudo bash
```
       
''')
f.close()
