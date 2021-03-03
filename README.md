# SQL Injections and XSS Cross Site Scripting.

Created by: Michael Brown and Kate Reynolds

## Files Included

### SQL Injection Files

*Used to log in as an arbitrary user*

The first 2 files exploit the fact that the when logging in, username and password are sent in plain text in post
requests to a SQL server

- `sql_0.txt`

A basic SQL injection that can be used as a password if single quotes are not escaped

- `sql_1.txt`

SQL injection that can be used to **Even if single quotes are escaped**

### XSS Cross-Site Scripting Files

*Used to steal cookies. In this case, last_search and username are sent to an external server*

- `xss_0.txt`

- `xss_1.txt`