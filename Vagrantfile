Vagrant.configure("2") do |config|
  config.vm.box          = "ubuntu/jammy64"
  config.vm.hostname     = "projet-cloud"
  config.vm.network "private_network", ip: "192.168.56.10"
  config.vm.boot_timeout = 600

  config.vm.provider "virtualbox" do |v|
    v.name   = "projet-cloud"
    v.memory = 5120
    v.cpus   = 2
    v.customize ["modifyvm", :id, "--uartmode1", "file", File::NULL]
  end

  config.vm.provision "shell", inline: <<-SHELL
    set -e

    # DNS fiable (Google) via systemd-resolved
    mkdir -p /etc/systemd/resolved.conf.d
    printf "[Resolve]\\nDNS=8.8.8.8 8.8.4.4\\n" > /etc/systemd/resolved.conf.d/dns.conf
    systemctl restart systemd-resolved

    # Docker, Docker Compose v2, Git, curl
    apt-get update
    apt-get install -y docker.io docker-compose-v2 git curl
    systemctl enable --now docker
    usermod -aG docker vagrant
    # Socket Docker : permissions par defaut (root:docker 660). Pas de chmod 666.

    # Swap de 2 Go (la VM sature sans)
    if [ ! -f /swapfile ]; then
      fallocate -l 2G /swapfile
      chmod 600 /swapfile
      mkswap /swapfile
      swapon /swapfile
      echo '/swapfile none swap sw 0 0' >> /etc/fstab
    fi
  SHELL
end
