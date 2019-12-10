# DFX Service

> BASE-URL (*unavailable currently*) : http://test.xymind.cn/

## 1 Measure
creating a new measurement by a video stream.

this is generally provided by a common streaming media protocol,like RTSP/RTMP,etc.Make sure that streaming media can be accessed publicly with a good speed and quality.

### 1.1 Requirement
if the webcam is used, the measurement duration is automatically set to 30 seconds (~900 frames at 30 fps). The resolution is then set to the camera default.

property|requirement
-:|:-
FPS|≥ 25 (fps)
Resolution|≥ 640 x 480 (px)

### 1.2 Declaration
since it's surely would take a pretty long time to measure a video stream,we cut every 5s as a chunk to do measure. it means clients would recicve results more than once(≥ 6 times). therefor,here we choose to keep long connections with clients by websocket(based on [signalr.core](https://docs.microsoft.com/zh-cn/aspnet/core/signalr/introduction?view=aspnetcore-3.0)).

clients would get chunk measurements every 150 effective frames and would get a summarization after process 900 effective frames.

### 1.3 Connection
signalr.core sdk is strongly recommended. it covers most of common platforms,such as Java/.Net/Python/JavaScript.If you have special custom needs,you definitely could use orginal websocket.

```url
http://test.xymind.cn/measure
ws://test.xymind.cn/measure
```

plateform | demo
:-|:-
Java/Android | https://github.com/aspnet/SignalR-samples/tree/master/AndroidJavaClient
.Net | https://github.com/aspnet/SignalR-samples/tree/master/ChatSample
JavaScript|https://docs.microsoft.com/zh-cn/aspnet/core/signalr/javascript-client?view=aspnetcore-3.0
Python|https://dev.to/mandrewcito/singlar-core-python-client-58e7

### 1.4 Interface
* Server
    ```csharp
    // test connection
    void Test()

    // create a measurement
    [Authorize]
    void Measure(string rtmp)
    ```

* Client
    ```csharp
    //callled by test connection
    void Test(string message)

    /*
    * called when errors occur
    * 
    * error example: {'code':400,'message':'something went wrongly'}
    */
    void ErrorHandler(string error)

    /*
    * called after every chunk measurement
    * measurement example: {"Chunk Number": 1, "Results": "Success", "SNR": 3.22, "HEART_RATE": 0.96, "HR_BPM": 57.36}
    */
    void ProcessChunkMeasurement(string measurement)

    /*
    * called after a whole measurement
    * measurement example: {"data": {"content": {"Id": "e12f0b5a-c3f1-4482-9b74-aaada3353ac0", "Results": {"HR_BPM": 64.1449, "SNR": 2.0117, "HEART_RATE": 1.069, "MENTAL_STRESS_INDEX": 2.6017}, "StatusID": "COMPLETE", "DataSizeBytes": 152136, "CreateTime": "2019-11-28 07:06:42"}, "message": null}, "statusCode": 200}
    */
    void ProcessMeasurement(string measurement)
    ```

### 1.5 Measurement

here are some instructions of the measurement in the table blew.

Property|Description
:-|:-
Id|identity for current measurement
StatusId|measurement status[1]
HR_BPM|Average heart rate in beats-per-minute (bpm). Measurable Range: 40-140bpm (0.67-2.33Hz)
SNR|Average blood flow signal SNR over the duration of the measurement
HEART_RATE|Average heart rate in Hz. Measurable Range: 40-140bpm (0.67-2.33Hz)
MENTAL_STRESS_INDEX|Average Mental Stress Index as determined by heart rate variability features. The range is [1.0 - 5.9], the higher the value, the greater the stress
Message|error message if exists
DataSizeBytes|data size transited
CreateTime|created time

* *[1] measurement with "MENTAL_STRESS_INDEX" will return "COMPLETE",otherwise it will be "WARNING"*
* *[2] getting "MENTAL_STRESS_INDEX" needs 30s at least*

### 1.6 Stream Media
* Push Stream
    * URL: rtmp://test.xymind.cn:1935/stream
    * Stream Key: GUID
* Watch Stream 
    * URL: rtmp://test.xymind.cn:1935/stream/GUID

## 2 Auth
authentication and authorization.

* API docs can refer to the [swagger docs](https://service.xymind.cn/swagger/index.html#/Auth).
* the parameter named `purpose` of the API which is charge of sending verification code has 2 options.
    ```csharp
    enum SmsPurpose
    {
        SignUp = 0,
        ResetPassword = 1
    }
    ```

* the APIs below require authorization.

    URL|Method|Description
    :-|:-|:-
    /Auth|PUT|update user profile
    /Auth​/ResetPassword|PUT|reset user password
    ​/Auth​/ChangePassword|PUT|change user password
* we use JWT for authorization.you can call APIs with Bearer Token in header named `Authorization`.

## 3 Record
recording measurements and videos(if necessary) from clients.users can look back their measure history.

* API docs can refer to the [swagger docs](https://service.xymind.cn/swagger/index.html#/Record)
* all APIs in this module require authorization.

* the API which is in charge of backup a measurement video requires a `video` parameter from `form-data`.

## 4 Health
health check for current service.

> All time fields involved in current service use UTC time.