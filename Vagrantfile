Vagrant.configure(2) do |config|
  config.vm.box = "ubuntu/trusty64"
  config.vm.network :forwarded_port, host: 4567, guest: 8080
  config.vm.synced_folder ".", "/home/vagrant/src/RecipeCrawler/"

  config.vm.provision "shell", inline: <<-SHELL
    # Change to python3 as default
    sudo rm /usr/bin/python
    sudo ln -s /usr/bin/python3 /usr/bin/python

    # install YAML
    sudo apt-get install -y python3-dev libxml2-dev libxslt-dev
    wget  http://pyyaml.org/download/pyyaml/PyYAML-3.11.tar.gz
    tar xvf PyYAML-3.11.tar.gz
    cd PyYAML-3.11/
    sudo python setup.py install
    cd ..
    rm -r PyYAML-3.11/ PyYAML-3.11.tar.gz

    # install setuptools
    wget https://bootstrap.pypa.io/ez_setup.py -O - | sudo python
    sudo rm setuptools*.zip

    #install jenkins
    # wget -q -O - https://jenkins-ci.org/debian/jenkins-ci.org.key | sudo apt-key add -
    # sudo sh -c 'echo deb http://pkg.jenkins-ci.org/debian binary/ > /etc/apt/sources.list.d/jenkins.list'
    # sudo apt-get update
    # sudo apt-get install jenkins
  SHELL
end
