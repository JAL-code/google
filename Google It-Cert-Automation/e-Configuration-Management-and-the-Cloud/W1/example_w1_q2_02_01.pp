class sysctl {
   
  # Make sure the directory exists, some distros don't have it
  file { '/etc/sysctld.d':
    ensure => present,
  }
}
