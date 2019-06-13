.. _algo:

client( ).algo( )
===================

透過 client().algo() 進行演算法取用。
algo 中必須輸入演算法網址。

如：algo("alog://aihub/24b54d6b-8cb3-11e9-a1e2-f45c89a9272d/")

.. note::

    在取用演算法前，請先至平臺網頁與演算法進行簽約。

|

post(\"執行內容\")
----------------------

透過 post 功能，進行演算法呼叫，並回傳運算結果。

Example Usage
~~~~~~~~~~~~~~~

::

    from aihub import client
    from json  import dumps

    #define the aihub client
    ai_client = client('使用者權仗')

    data = {}

    #read the testing data from news
    with open('news.txt','r') as f:
        file_sream = f.read()
        data['test'] = ai_client.file().collection('news').filename('news.txt').putFile()

    #convert dict object to json object
    json_data = dumps(data)

    #define algo object and post json_data to get result.
    algo = ai_client.algo('alog://aihub/24b54d6b-8cb3-11e9-a1e2-f45c89a9272d/')
    result = algo.post(json_data)

|