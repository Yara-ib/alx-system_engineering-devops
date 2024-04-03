# Add a custom HTTP header with Puppet

exec { 'update system':
        command => 'sudo apt-get update',
}

package { 'nginx':
	ensure => 'installed',
}

file {'/var/www/html/index.html':
	content => 'Hello World!'
}

exec {'redirect_me':
	command => 'sed -i "24i\	rewrite ^/redirect_me http://yrap.tech/ permanent;" /etc/nginx/sites-available/default',
	provider => 'shell'
}

exec {'HTTP header':
    environment => ["HOST=${hostname}"],
    command     => 'sudo sed -i "s/include \/etc\/nginx\/sites-enabled\/\*;/include \/etc\/nginx\/sites-enabled\/\*;\n\tadd_header X-Served-By \"$HOST\";/" /etc/nginx/nginx.conf',
}

service {'nginx':
	ensure => running,
}
