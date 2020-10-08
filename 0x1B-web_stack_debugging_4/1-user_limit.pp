# Change the limit on number of open files
exec { 'hard':
  command => 'sed -i "/holberton hard nofile 5/d" /etc/security/limits.conf',
  path    => '/bin',
}
exec { 'soft':
  command => 'sed -i "/holberton soft nofile 4/d" /etc/security/limits.conf',
  path    => '/bin',
}
