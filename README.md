# Auto fill temperture form

use `python` and `crontab` can fill the temperture form every morning
### in bash
```bash
crontab -e
``` 
### edit crontab file
```vim
30 7 * * * /your/python/path/python3.x /your/file/path/.py # use Absolute Path
```
### in bash
```bash
sudo /etc/init.d/cron restart
``` 