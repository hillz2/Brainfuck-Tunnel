# Brainfuck Tunnel

SSH Tunneling for Dynamic Port Forwarding (Free charge Internet Access).


Requirements
------------

### Packages

    nc (openbsd-version) (be aware if you are installing wrong nc)
    git
    openssh
    sshpass
    python3
    corkscrew
    python3-pip


### Using Termux on Android?

    $ pkg install pip git python openssh sshpass corkscrew


### Using Cygwin on Windows?

**1. apt-cyg**

    $ wget rawgit.com/transcode-open/apt-cyg/master/apt-cyg -P /bin/; chmod +x /bin/apt-cyg


**2. required packages**

    $ apt-cyg install nc tar curl make openssh python3 autoconf gcc-core corkscrew python3-pip


**3. sshpass**

    $ curl -LO http://downloads.sourceforge.net/sshpass/sshpass-1.06.tar.gz
    $ md5sum sshpass-1.06.tar.gz
    $ tar xvf sshpass-1.06.tar.gz
    $ cd sshpass-1.06
    $ ./configure
    $ make
    $ make install


Python 3 Modules
----------------

    $ python3 -m pip install --upgrade pip
    $ python3 -m pip install requests beautifulsoup4
    $ python3 -m pip install -U requests[socks]


Configurations
--------------

Run `reset.py` first to export all default settings.

**1. Tunel Type**

    0: Direct     -> SSH
    1: Direct     -> SSH (SSL/TLS)
    2: HTTP Proxy -> SSH


**2. SOCKS5 Port**

    "socks5_port_list_external": [
      "#1080",
      "#1081",
      "#1082",
      "#1083",
      "#1084",
      "#1085"
    ]

    "socks5_port_list": [
      "1080",
      "1081",
      "1082",
      "1083",
      "1084",
      "1085"
    ]

If `socks5_port_list_external` like that (no port or all port commented), You will execute 1 SSH Client (default port: `1080`).
If `socks5_port_list` like that. You will execute 5 SSH Clients.
Add ports to execute more SSH Clients.


**3. Proxy Command**

Please googling for this topic or see `config/config.json` (run `reset.py` first).

    proxy_host: {inject_host}
    proxy_port: {inject_port}


Usage
-----

    $ git clone https://github.com/AztecRabbit/Brainfuck-Tunnel brainfuck-tunnel
    $ cd brainfuck-tunnel; ls -l
    $ python3 (file-name)


Update
------

    $ cd brainfuck-tunnel
    $ git pull
    $ python3 reset-database.py


Note
----

    Ctrl-C to Change Server
    Ctrl-Pause to Exit


Contact
-------

Facebook Group : [Internet Freedom]


[Internet Freedom]: https://www.facebook.com/groups/171888786834544/
