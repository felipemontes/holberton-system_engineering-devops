# Renaming file in wp server
exec { 'rename':
  command  => 'sudo mv /var/www/html/wp-includes/class-wp-locale.php /var/www/html/wp-includes/class-wp-locale.phpp',
  provider => shell,
}
