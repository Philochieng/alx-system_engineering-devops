#!/usr/bin/env bash
# Configures HAProxy on the load balancer server

# Update package lists
apt update

# Install HAProxy
apt install -y haproxy

# Backup the default HAProxy configuration
mv /etc/haproxy/haproxy.cfg /etc/haproxy/haproxy.cfg.backup

# Create a new HAProxy configuration file
touch /etc/haproxy/haproxy.cfg

# Configure HAProxy to balance traffic among the web servers
cat <<EOF > /etc/haproxy/haproxy.cfg
frontend http_front
    bind *:80
    default_backend http_back

backend http_back
    balance roundrobin
    server web1 165937-web-01:80 check
    server web2 165937-web-02:80 check
EOF

# Restart HAProxy service
service haproxy restart

