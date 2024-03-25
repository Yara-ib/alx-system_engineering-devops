#  Manifest make changes to our configuration file.

exec { 'ssh_config':
    command  => 'ssh -F ~/.ssh/school -o PasswordAuthentication=no',
    provider => 'shell'
}
