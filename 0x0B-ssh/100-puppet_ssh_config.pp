# Ensure SSH client configuration file
file { '/etc/ssh/ssh_config':
  ensure => file,
}

# Configure SSH client to use the private key ~/.ssh/school
file_line { 'Declare identity file':
  path  => '/etc/ssh/ssh_config',
  line  => '    IdentityFile ~/.ssh/school',
  match => '    IdentityFile.*',
}

# Configure SSH client to refuse password authentication
file_line { 'Turn off passwd auth':
  path  => '/etc/ssh/ssh_config',
  line  => '    PasswordAuthentication no',
  match => '    PasswordAuthentication.*',
}
