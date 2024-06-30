#Using Puppet, install flask from pip3

node default {

  # Ensure pip3 is installed
  package { 'python3-pip':
    ensure => installed,
  }

  # Install Flask 2.1.0 using pip3
  exec { 'install_flask':
    command => '/usr/bin/pip3 install flask==2.1.0',
    unless  => '/usr/bin/pip3 show flask | grep Version | grep -q 2.1.0',
    require => Package['python3-pip'],
  }
}

