# Create ssh for client with puppet
file {'~/.ssh/config':
  ensure  => present,
  replace => 'yes',
  path    => '~/.ssh/config',
  content => 'Host *
     HostName 34.73.23.33
     User Daniel
     IdentityFile ~/.ssh/holberton',
  mode    => '7000',
}
