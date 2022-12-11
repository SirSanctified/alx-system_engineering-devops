# client ssh configuration file
file {'/etc/ssh/ssh_config':
    ensure  => file,
    path    => '/etc/ssh/ssh_config',
    mode    => '0744',
    content => 'Host 100.25.4.131
        IdentityFile ~/.ssh/school
        PasswordAuthentication no'
}
