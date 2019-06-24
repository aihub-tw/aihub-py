.. _file:

client( ).file
===================

平臺的檔案存取，
除了使用網站介面進行操作，
也可以使用本套件進行處理。

.. note::

    file 的執行身份為 client 宣告時之身份。

    若在演算法端，其身份則為操作演算法的使用者。

|

getFile(\\'檔案路徑\\')
-----------------------

此功能用以抓取檔案，
抓取的來源不限於使用者個人檔案、演算法產生之檔案、演算法範例檔案。
只要代入檔案路徑，
便可以抓取該檔案 Binary 物件。

Example Usage
~~~~~~~~~~~~~~~

::

    from aihub import client

    #define the aihub client
    ai_client = client('使用者權杖')

    #use getFile to get the matrix.csv in testing_data folder. 
    file = ai_client.file.getFile('storge://.my/aihub/testing_data/matrix.csv')

|

putFile(\\'檔案路徑\\')
-----------------------

此功能用以上傳檔案，
透過此功能可將檔案上傳至使用者個人資料夾，
亦可透過此功能將演算法執行結果放至使用者演算法資料夾。

.. note::

    使用此功能時，
    必須使用 .fileName(\\'檔案名稱\\') 填入檔案名稱。
    若無填入檔案名稱，
    會回傳 Please use .fileName() to set your filename.


collection(\\'資料夾名稱\\')
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

當 client 在使用者端時，
進行檔案上傳的動作會將資料放置於使用者個人資料夾。
但使用者必須使用 collection( ) 定義存放檔案的資料夾。
若該資料夾不存在，
系統會自動協助進行建立。

.. warning::

    若 client 在演算法端時，
    則不可呼叫此方法，
    會造成功能執行錯誤。

Example Usage
~~~~~~~~~~~~~~~

::

    import pickle
    from aihub import client

    #define the aihub client
    ai_client = client('使用者權杖')

    #data from algorithm
    data = range(1, 100)
    result = pickle.dumps(data)

    #use putFile to put the result.csv in result_data folder. 
    file_path = ai_client.file.collection('result_data').fileName('result.csv').putFile(result)

    #file_path will be {'status': 'success', 'file_path': 'storage://.my/aihub/result_data/result.csv'}
    print(file_path)


fileName(\\'檔案名稱\\')
~~~~~~~~~~~~~~~~~~~~~~~~

在進行檔案上傳時，
必須使用 filename( ) 定義檔案名稱。

.. note::

    若上傳檔案時沒有呼叫此功能，會出現 Please use .fileName() to set your filename. 的錯誤。

    當呼叫此功能，且檔案名稱為空，會出現 Please enter your file name. 的錯誤。

Example Usage
~~~~~~~~~~~~~~~~

::

    import pickle
    from aihub import client

    #define the aihub client
    ai_client = client()

    #data from algorithm
    data = range(1, 100)
    result = pickle.dumps(data)


    #use putFile to put the result.csv in user algorithm folder. 
    file_path = ai_client.file.fileName('result.csv').putFile(result)

    #file_path will be {'status': 'success', 'file_path': 'storage://.proj/20058228-8c20-11e9-8796-f45c89a9272d/aihub/933ac55c-9661-11e9-af7d-f45c89a9272d/result.csv'} 
    print(file_path.get('file_path'))

|

deleteFile(\\'檔案路徑\\')
---------------------------

若要進行檔案刪除，
可呼叫此功能進行檔案刪除的動作。

Example Usage
~~~~~~~~~~~~~~~

::

    from aihub import client

    #define the aihub client
    ai_client = client('使用者權杖')

    #use deleteFile to delete the result.csv. 
    result = ai_client.file.deleteFile('storage://.my/aihub/result_data/result.csv')
