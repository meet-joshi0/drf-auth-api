#user registration and login api using django rest framework

## Installation

use following commands to setup working installation of api

```bash
python3 -m pip install -r requirements.txt
python3 manage.py migrate
python3 mabage.py runserver
```



## Usage Instruction


To Register new account use  ``` api/register/ ``` endpoint <br/>
To obtain access token use ```api/token/``` endpoint <br/>
To Refresh expired token use ```api/token/refresh/``` endpoint <br/>

 
## Additional Information
django rest natively support session and basic auth but jwt is used in support of scalability and self contained aspect.

Default expire time for token is 30 minutes which can be changed from settings. token can be manually expired by using blacklisted app, available with jwt package.

## Testing
To check working of this demo project ```api/test/``` endpoints can be used. 


use following curl request for local testing

```
curl request: 

curl \
  -H "Authorization: Bearer your acces_token " \
 http://127.0.0.1:8000/api/test/

example:

 curl \
  -H "Authorization: Bearer eyJ0eXY3NmM0NmY0YjOjE3fQ.su3i_D53_BukHi9HwNdCyqC9e6R4_LLjMjg" \
 http://127.0.0.1:8000/api/test/




```


## License
[MIT](https://choosealicense.com/licenses/mit/)
