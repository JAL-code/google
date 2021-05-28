node default {
  # two classes included
  class { 'sudo': }
  class { 'ntp': 
    # servers parameters
    servers => ['ntp1.example.com', 'ntp2.example.com']
  }
}
