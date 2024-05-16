# User limit
exec { 'user_limit_soft':
    command  => 'sed -i "/holberton soft/s/4/50000/" /etc/security/limits.conf',
    provider => shell
}
exec { 'user_limit_hard':
    command  => 'sed -i "/holberton hard/s/5/50000/" /etc/security/limits.conf',
    provider => shell
}
