# Search  and repair

exec { 'repair wp-settings':
  command => "sed -i 's/.phpp/.php/' /var/www/html/wp-settings.php",
  path    => '/bin/',
}
