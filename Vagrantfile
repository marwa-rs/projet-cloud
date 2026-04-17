Vagrant.configure("2") do |config|
  config.vm.box = "ubuntu/jammy64"
  config.vm.network "private_network", ip: "192.168.56.10"
  config.vm.hostname = "projet-cloud"
  config.vm.boot_timeout = 600

  config.vm.provider "virtualbox" do |v|
    v.memory = 5120
    v.cpus = 2
    v.name = "projet-cloud"
    v.customize ["modifyvm", :id, "--uart1", "0x3F8", "4"]
    v.customize ["modifyvm", :id, "--uartmode1", "file", File::NULL]
  end

  config.vm.provision "shell", inline: <<-SHELL
    apt-get update
    apt-get install -y docker.io docker-compose git curl
    systemctl enable docker
    systemctl start docker
    usermod -aG docker vagrant
    chmod 666 /var/run/docker.sock
    echo "Docker prêt !"
  SHELL
end
