class timezone {

  file { '/etc/timezone':
    ensure => file,
    content => "UTC\n",
    replace => true,
  }

}
