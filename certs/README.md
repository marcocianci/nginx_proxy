# step-by-step to generate a self-signed SSL/TLS
## These commands are used to generate a self-signed SSL/TLS certificate for a domain name.

- The first command generates a private key named `localhost.key` with a length of 2048 bits using the RSA algorithm.
```
openssl genrsa -out localhost.key 2048
```
- The second command creates a certificate signing request (CSR) named `localhost.csr` using the private key generated in the previous step. The `-config` option specifies the configuration file to use, and the `-subj` option specifies the subject of the certificate request. In this case, the subject is set to `/C=BR/ST=SaoPaulo/L=SaoPaulo/O=Cianci TI/CN=dev.cianci.com.br`.
```
openssl req -new -key localhost.key -out localhost.csr -config san.cnf -subj "/C=BR/ST=SaoPaulo/L=SaoPaulo/O=Cianci TI/CN=dev.cianci.com.br"
```
- The third command signs the certificate using the private key and the CSR, and generates a self-signed X.509 certificate named `localhost.crt`. The `-extensions` and `-extfile` options specify the extensions and configuration file to use. In this case, the `req_ext` extension is used to specify the Subject Alternative Name (SAN) and the `san.cnf` configuration file contains the details of the SAN. The `-days` option specifies the number of days the certificate should be valid for, and the `-sha256` option specifies the hash algorithm to use.
```
openssl x509 -req -in localhost.csr -signkey localhost.key -out localhost.crt -extensions req_ext -extfile san.cnf -days 825 -sha256
```

## Whel done! Mooonsster kill.
> Add file `localhost.crt` to Trusted Root Certification Authorities folder in the Certificate Manager


cp ./localhost.crt ~/Documents/cert

```
cp ./cianci_dev_localhost.* ~/Documents/cert
cp ./cianci_dev_localhost.crt ~/Documents/cert
cp ./cianci_dev_localhost.crt ~/Documents/cert

```


