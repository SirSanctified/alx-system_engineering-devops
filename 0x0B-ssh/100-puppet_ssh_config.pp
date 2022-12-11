# client ssh configuration file
file {'/home/sir_sanctified/.ssh/config':
    ensure  => file,
    path    => '/home/sir_sanctified/.ssh/config',
    mode    => '0744',
    owner   => 'sir_sanctified',
    group   => 'sir_sanctified',
    content => 'Host 100.25.4.131
        IdentityFile ~/.ssh/school
        PasswordAuthentication no'
}
