if $fact['is_virtual']{
  package { 'smartmontools':
    ensure => purged,
    
  }
} else {
  package { 'smartmontools':
    ensure => installed,
  }
}
