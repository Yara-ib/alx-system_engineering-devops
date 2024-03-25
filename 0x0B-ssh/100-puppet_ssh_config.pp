#  Manifest make changes to our configuration file.

exec { 'ssh':
    command  => 'ssh -F ~/.ssh/school -o PasswordAuthentication=no',
    provider => 'shell'
}
