# Concurrent Web requests

## Chapter 16
##### What is HTML?
HyperText Markup Language. Used to develop web pages and applications, using tags 

##### What are HTTP requests?
HyperText Transfer Protocol, Session based protocol used to send and receive HTML files

##### What are HTTP Response status codes?
Protocol defined numbers indicating status of HTTP request/response. Codes are categorized into 5 types:
 - 1xx Informational - Typically used mid req/resp. Header received, request being processed, etc
 - 2xx Successful - Request was received, understood, and processed by server
 - 3xx Redirectional - These aren't the server's you're looking for
 - 4xx Client Error - Client request could not be parsed. See 404, request not supported ('that page does not exist')
 - 5xx Server Error - Valid request, but server is unable to respond 

##### How does the requests module help with making web requests
Functions as API to make HTTP requests within a python environment

##### What is a ping test and how is one typically made?
Traditionally, ping tests are ICMP messages that operate within the network layer (no TCP/UDP or ports)
In this context, we will ping over HTTP, considering response codes equivalent to ICMP codes. 

##### why is concurrency applicable in making web requests?
Concurrency through multithreading or multiprocessing allows other jobs to start up while awaiting server response

##### What are the considerations that need to be made while developing applications that make concurrent web requests?
Formatting and Security

 - Formatting: Websites are prone to change their layout with no advance warning. If a webscrape is crucial to a job, 
 check if the site has some sort of API to access, otherwise be prepare to reformat any parsing

 - Security: Webscraping exists in a somewhat nebulous state. While itself innocuous, some site owners may take exception to 
aggressive scraping; as well, excessive server requests in a short time may trigger DDOS defenses 

##Scripts
### 01.py
Simple get request of google.com, utilizing requests module

### 02.py
Get requests from httpstat.us of multiple status codes

### 03.py
Remake of 02, showing Concurrency vs threaded performance 

### 04.py
Extend Threaded build in 03 to custom class

### 05.py
Reuse of 04 but with a 20sec delay request. This blocks our threads from joining, preventing any on screen results

### 06.py
Add custom handler to manage threded HTTP request classes; handler manages thread starts, dameon state, and timeouts 
(compare to book's simple function)
