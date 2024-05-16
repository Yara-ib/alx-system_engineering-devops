# Unleash the power of HTTP requests' Ulimit that can be handled
exec { 'change_limit':
    command  => 'sed -i s/15/2048/g /etc/default/nginx',
    provider => shell
}
