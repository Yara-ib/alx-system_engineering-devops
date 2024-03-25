#  Manifest make changes to our configuration file.

exec { '2-ssh_config':
    command  => 'ssh -F ~/.ssh/school -o PasswordAuthentication=no',
    provider => 'shell'
}
