#  Manifest to perform a 301 redirect when querying /redirect_me.

exec { 'update':
    command  => 'sudo apt-get -y update',
    provider => 'shell'
}

package { 'nginx':
    ensure => 'installed',
}

exec { 'update':
    command  => 'sudo ufw allow 'Nginx HTTP'',
    provider => 'shell'
}

file {'index.html':
    ensure  => present,
    path    => '/var/www/html/',
    owner   => root,
    group   => root,
    mode    => '0777',
    content => 'Hello World!'
}

file_line { 'redirect_me':
  ensure  => 'present',
  require => Package['nginx'],
  path    => '/etc/nginx/sites-available/default',
  after   => 'root /var/www/html;',
  line    => 'rewrite ^/redirect_me https://www.youtube.com/watch?v=QH2-TGUlwu4 permanent;',
  notify  => Service['nginx'],
}

service { 'nginx':
  ensure  => running,
  require => File_line['redirect_me'],
}
