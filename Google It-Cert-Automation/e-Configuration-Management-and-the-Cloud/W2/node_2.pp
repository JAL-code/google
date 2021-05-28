# specific nodes in the fleet are identified by their FQDNs,
# FQDN = fully qualified domain names.
node webserver.example.com {
  # two classes included
  class { 'sudo': }
  class { 'ntp':
    # servers parameters
    servers => ['ntp1.example.com', 'ntp2.example.com']
  }
  class { 'apache': }
}
