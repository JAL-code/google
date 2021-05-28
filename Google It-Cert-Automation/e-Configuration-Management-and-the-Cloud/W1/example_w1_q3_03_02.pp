exec { 'move example file':
  command => 'mv /home/user/example.txt /home/user/Desktop',
  only    => 'text -e /home/user/example.txt',
}
