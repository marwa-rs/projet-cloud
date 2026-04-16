Vagrant.configure("2") do |config|
  config.vm.box = "ubuntu/jammy64"
  config.vm.network "private_network", ip: "192.168.56.10"
  config.vm.hostname = "projet-cloud"

  config.vm.provider "vmware_desktop" do |v|
    v.memory = 4096
    v.cpus = 2
  end

  config.vm.provision "shell", inline: <<-SHELL
    apt-get update
    apt-get install -y docker.io docker-compose git curl
    systemctl enable docker
    systemctl start docker
    usermod -aG docker vagrant
  SHELL
end
