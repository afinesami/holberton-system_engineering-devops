#puppet advance
exec { 'update':
  command  => 'sudo apt-get update',
  provider => shell,
}
-> package {'nginx':
  ensure => present,
}
-> file_line { 'header line':
  ensure => present,
  path   => '/etc/nginx/sites-available/default',
  line   => "	location / {
  add_header X-Served-By ${hostname};",
  match  => '^\tlocation / {',
}
-> exec { 'restart service':
  command  => 'sudo service nginx restart',
  provider => shell,
}