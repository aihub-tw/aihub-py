.. _client:

client( )
==========

client 提供使用者與AIHUB進行溝通，
舉凡存取演算法、存取檔案皆須使用 Client 進行處理。

.. note::

    client分為 **演算法端** 與 **使用者端**，

    **演算法端** 的 client 不帶有使用者權杖，
    會以操作演算法的用戶為身份，
    以該身份進行演算法與檔案的存取。

    **使用者端** 的 client 帶有使用者權杖，
    會以該權仗代表之使用者為身份，
    以該身份進行演算法與檔案的存取。

|

演算法端的 client( )
----------------------

client在宣告時，
不能代入使用者權杖，
直接宣告該 Class 使用即可。

.. warning::

    若在演算法端代入使用者權杖，
    會造成Client宣告失敗。
    
    回傳 Can not set the self_token in the Algorithm!

Example Usage
~~~~~~~~~~~~~~~

::

    from aihub import client

    #define the aihub client
    ai_client = client()

|

使用者端的 client( )
----------------------

client在宣告時，
必須代入使用者權杖，
方可宣告該 Class。

.. warning::

    若在使用者端未代入使用者權杖，
    會造成Client宣告失敗。
    
    回傳 Client must have a token! Please use client("token") to enter the token!

Example Usage
~~~~~~~~~~~~~~~

::

    from aihub import client

    #define the aihub client
    ai_client = client('使用者權杖')


