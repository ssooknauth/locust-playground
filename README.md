# locust-playground
Demo using locust.io (open source performance testing framework) and learning python 3 

Setup:

- Install python version 3 (https://docs.python-guide.org/starting/install3/osx/)
- Install pip (https://pip.pypa.io/en/stable/installing/)
- From the terminal **_pip install -r requirements.txt_**
  This will install locust.io (https://locust.io/)  and pytest (all the dependencies I need in one file  )
 


Running a simple performance (load test: a very very small load don't want bring any server down(unless permitted) or denial of service )
 - Start the flask server via this command: _**python3 server/simple_server.py**_
 - From the terminal: _**locust -f loadtest.py --host http://localhost:9999 --headless -u 10 -r 10 -t 4s**_  
The above test will run against our test server named localhost:9999 (--host), no web interface ( --headless), 10 users (-u), 10 spawns (-r, number of users per second ), 4s (stop after 4 seconds)

Credit: 
- https://docs.locust.io/en/stable/quickstart.html
- https://medium.com/better-programming/introduction-to-locust-an-open-source-load-testing-tool-in-python-2b2e89ea1ff

