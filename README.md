# fuzzbot
A Web Authentication Fuzzbot Project

This project was inspired by a project done by Engineer Man on YouTube to obfuscate logfiles or databases connected to scammer clone phishing sites. These login pages clone popular websites and pretend to authenticate users while really storing their login and password info in a logfile or database. The basic idea of the project is to obfuscate legitimate user info the scammer has collected by flooding the login page with plausibly legitimate login information and randomly generated passwords. By stuffing their logfiles and databases full of illegitimate information, it becomes extremely difficult (if not impossible) to discern between false credentials and legitimate ones.

My version of this project includes some feature enhancements, modernization for Python 3.9, and the addition of a user interface to allow the tool to be recycled for use against any site instead of being hard coded to work against a single site. I used JSON files to store the 1000 most popular male, 1000 most popular female, and 18000 most popular surnames in the United States in 2019. Also, there is a JSON file with the 100 most popular internet email domains for 2020. The user logins can be configured to include a full first and last name, first or last initials, and a trailing digit as desired. If a username is required to be in an email format, the operator can select to randomize email domains from the top 100 internet email domains, or enter a single domain for all attempts to use. Passwords are configured to be randomly selected 16 charachters in length, enough to satisfy most login form sanitization requirements. There is also an option to run the tool continually until the user interrupts, or to send a preset number of attempts to the target server.

Aside from this projects application as a tool to combat clone phishing, there is also an application for penetration testing. This is a lightweight, robust tool for stress testing website and webapp logins that use HTTP POST to send client information for web authentication. The application here is to test server log functionality, and with the potential to run multiple occurances simultaneously this application can test for denial of service resiliance in the scenario of an attack on the web authentication function of a site.

Please enjoy the project, it's brand new at this time and will continue to be updated as I add functionality or fix things that break.
As with any project of this nature, please use it legally and responsibly, by executing this source code you agree to indemnify me from any losses, damages, or legal responsobility arising from your actions.

Constructive criticism always welcome! dion315@gmail.com

<hr>

Usage:
<ol>
  <li>Open Chrome (This can be done in other browsers as well, I prefer Chrome but instructions for other browsers will be similar)
  <li>Press F12 to open developer console.
  <li>Select the Network tab, and be sure Preserve Log is checked. If Preserve Log is not present, click the gear icon in settings and check the Preserve Log box under Network.
  <li>Navigate to the login page you wish to target.
  <li>Attempt to log in with bad creds (ex. User: test, Pass: test)
  <li>You will now have to do some digging. If the login page is a PHP form for example, you can look at the PHP files. If it's HTML you might find an html file or something as    simple as a document called login. Click on these and look at the header information for form data (usually on the bottom of the header info).

It should look something like this:
```
url: http://www.somewebsite.com/login
user: test
pass: test
```
<li>Now execute python weblogin_fuzzer.py
<li>Enter the full URL from the form data *exactly* as it appeared. Omitting the http or https, or any trailing data will prevent this from working.
<li>Enter the arguments used to pass the username and password. You'll know them because we used test as our username and password so we could identify the arguments user for username, and pass for password. You don't need to enter the : just the names of the arguments.
<li>Answer a few more basic configuration questions and you're off! Easy!
