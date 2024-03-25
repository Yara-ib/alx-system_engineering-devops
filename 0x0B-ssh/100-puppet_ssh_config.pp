#  Manifest make changes to our configuration file.

exec { 'ssh':
    command  => 'ssh -F ~/.ssh/school -o PasswordAuthentication'
    provider => shell
}
