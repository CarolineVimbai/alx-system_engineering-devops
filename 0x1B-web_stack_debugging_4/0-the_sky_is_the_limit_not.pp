# Will make requests to my server
exec { 'change size the requests':
    command => '/bin/sed -i "s/15/30000/g" /etc/default/nginx | service nginx restart'
}
