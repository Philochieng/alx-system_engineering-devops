# Puppet manifest to install and configure Nginx web server

# Install Nginx package
package { 'nginx':
  ensure => installed,
}

# Configure Nginx
file { '/etc/nginx/sites-available/default':
  ensure  => present,
  content => "
    server {
        listen 80 default_server;
        listen [::]:80 default_server;

        root /var/www/html;
        index index.html index.htm index.nginx-debian.html;

        server_name _;

        location / {
            try_files \$uri \$uri/ =404;
        }

        location = / {
            return 200 'Hello World!';
            add_header Content-Type text/plain;
        }

        location /redirect_me {
            return 301 https://www.example.com;
        }
    }
  ",
}

# Enable the default site
file { '/etc/nginx/sites-enabled/default':
  ensure => 'link',
  target => '/etc/nginx/sites-available/default',
  notify => Service['nginx'],
}

# Restart Nginx service
service { 'nginx':
  ensure    => running,
  enable    => true,
  subscribe => File['/etc/nginx/sites-available/default'],
}

