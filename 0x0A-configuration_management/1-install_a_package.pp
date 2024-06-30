#Using Puppet, install flask from pip3

node default {

  package { 'python3-pip':
    ensure => installed,
  }


  exec { 'install_flask':
    command => '/usr/bin/pip3 install flask==2.1.0',
    unless  => '/usr/bin/pip3 show flask | grep Version | grep -q 2.1.0',
    require => Package['python3-pip'],
  }
}

