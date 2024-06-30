#Using Puppet, create a manifest that kills a process named killmenow

node default {
  exec { 'kill_killmenow_process':
    command => '/usr/bin/pkill killmenow',
    onlyif  => '/usr/bin/pgrep killmenow',
  }
}

