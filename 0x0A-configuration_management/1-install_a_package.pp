# Manifest to install flask from pip3

package { 'flask':
    ensure  => installed,
    require => Exec['pip3 install Flask==2.1.0']
}
