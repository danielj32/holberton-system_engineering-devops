# Create ssh for client with puppet
file { '/etc/ssh/ssh_config':
    ensure  => file,
    content => 'Host holb_server
    HostName 34.73.23.33
    User Daniel
    IdentityFile ~/.ssh/holberton
    PasswordAuthentication no',
}
