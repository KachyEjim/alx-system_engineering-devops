# Install an especific version of flask (2.1.0)
package {'python3-flask':
  ensure   => '2.1.0',
  provider => 'pip3'
}