# Using strace fixing why Apache is returning a 500 error

exec { 'swap_phpp_php':
    command  => 'sed -i s/phpp/php/g /var/www/html/wp-settings.php',
    provider => shell
}
