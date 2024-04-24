# Ensure that Werkzeug is installed as well
package { 'Werkzeug':
  ensure   => 'installed',
  provider => 'pip3',
}

# Install a specific version of Flask (2.1.0)
package { 'Flask':
  ensure   => '2.1.0',
  provider => 'pip3',
}
