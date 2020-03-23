# executing a command with puppet
exec { 'killmenow':
    command => 'pkill killmenow',
    path    => '/usr/bin',
    returns => [0, 1]
}