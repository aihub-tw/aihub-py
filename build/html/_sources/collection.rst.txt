.. _collection:

client( ).collection( )
=========================

在進行檔案上傳前，
可先透過 client().collection() 進行個人檔案夾的中的資料夾管理。
collection() 中須輸入資料夾名稱。
透過create()	、delete()、remame()進行處理。

.. note::

    collection( ) 功能僅在使用者端 client 有效。

|

create( )
----------------------

此功能可進行資料夾新增。

Example Usage
~~~~~~~~~~~~~~~

::

    from aihub import client

    #define the aihub client
    ai_client = client('使用者權杖')

    #create testing_data to user folder. 
    result = ai_client.collection('testing_data').create()

    #folder path will be "storage://.my/testing_data"
    print(result)

|

delete( )
----------------------

此功能可進行資料夾刪除。

.. warning::

    刪除資料夾時，會一同刪除裡面存放的檔案。
    請確定您的資料已經妥善保存！

Example Usage
~~~~~~~~~~~~~~~

::

    from aihub import client

    #define the aihub client
    ai_client = client('使用者權杖')

    #delete testing_data from user folder. 
    result = ai_client.collection('testing_data').delete()

|

rename(\\'新資料夾名稱\\')
---------------------------

此功能可進行資料夾重新命名。

Example Usage
~~~~~~~~~~~~~~~

::

    from aihub import client

    #define the aihub client
    ai_client = client('使用者權杖')

    #rename folder name from testing_data to all_data in user folder. 
    result = ai_client.collection('testing_data').rename('all_data')

|