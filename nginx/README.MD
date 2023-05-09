> ./default-domain-example.conf
```
upstream service_marcocianci_8202 {
    server csn.dev.marcocianci.com:8202;
}
```
This block defines an upstream server group called `service_marcocianci_8202`. It specifies that requests should be forwarded to the server `csn.dev.marcocianci.com` on port `8202`.
>;
```
server {
    listen 80;
    server_name csn.dev.marcocianci.com;
    return 301 https://$server_name$request_uri;
}
```
This server block listens on port 80 and handles HTTP requests for the domain `csn.dev.marcocianci.com`. It issues a 301 redirect to the corresponding HTTPS URL by using the return directive.
>;
```
server {
    listen 443 ssl;

    ssl_certificate /etc/nginx/ssl/marcocianci_local.crt;
    ssl_certificate_key /etc/nginx/ssl/marcocianci_local.key;

    server_name csn.dev.marcocianci.com;
    location / {
        proxy_pass http://service_marcocianci_8202;
        proxy_set_header Host $host;
        proxy_set_header X-Real-IP $remote_addr;
        proxy_set_header X-Forwarded-For $proxy_add_x_forwarded_for;
        proxy_set_header X-Forwarded-Proto $scheme;
    }
}

```
This server block listens on port 443 (HTTPS) and handles HTTPS requests for the domain `csn.dev.marocianci.com`. It uses SSL/TLS certificates specified by the `ssl_certificate` and `ssl_certificate_key` directives.

The `location` / block defines a reverse proxy configuration using the `proxy_pass` directive. It forwards requests to the upstream server group `service_marocianci_8202`. The `proxy_set_header` directives are used to pass various HTTP headers to the upstream server.

Overall, this configuration ensures that HTTP requests to `csn.dev.marocianci.com` are redirected to HTTPS, and the HTTPS requests are proxied to the `csn.dev.marocianci.com` server on port 8202, while preserving the original request headers.
