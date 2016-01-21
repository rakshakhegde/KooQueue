# KooQueue

Originally I thought of naming this project PhoQueue (which obviously stands for Phone Queue) but it just didn't sound right.

## Problem
Due to TRAI regulations, Kookoo does not send promotional or transactional SMSes after 9pm until 9am. And also Kookoo does not queue up these SMSes to send on the following day. So a business/startup/company cannot make sure that these SMSes reach their target audience after 9pm. Hence we need a service that can queue up these "pushes" to be completed on the following day.

This is a feature that is highly useful and is already implemented by Twilio, Plivo, Nexmo, etc (services similar to Kookoo). Hence this project, KooTweet, can be a great add-on to Kookoo's services.

## Solution
A scalable, highly concurrent and fault tolerant system (KooQueue) to queue up these messages and send them the following day between 9am-11am. The API almost mirrors the original Kookoo API, hence it is easy to shift to this service in your existing project.

## API
```
HTTP(S) request
https://hacks-rakheg.rhcloud.com/kooqueue/
The parameters to be provided are:
phone_no : The number to which we need to send the sms.
api_key : For security purposes. Use your API key in your Kookoo dashboard.
message : The message to be sent.
senderid : The 6 characters senderid which has been setup on your account. For example KOOKOO.
```
>Example:
>
>1) https://hacks-rakheg.rhcloud.com/kooqueue/?phone_no=9xxxxxxx90&api_key=your_api_key&message=testing
>
>2) https://hacks-rakheg.rhcloud.com/kooqueue/?phone_no=9xxxxxxx90&api_key=your_api_key&message=testing&senderid=KOOKOO