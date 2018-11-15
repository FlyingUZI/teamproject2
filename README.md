# teamproject2

## scraping file

docs/websocketLocal.py

## Development

1. `docker pull ergofriend/teamproject2`
2. `docker run -d -p 80:80 --expose 80 ergofriend/teamproject2 python manage.py runserver 0.0.0.0:80`
3. `curl http://35.236.39.253/api/test/`
4. `wscat --connect http://35.236.39.253/ws`
5. `curl http://35.236.39.253/api/publish/?msg=hi`
