# Public IP Utility 

A simple utility to update a public IP address on Google Sheets. This is useful for accessing port forwarded devices on a network with a dynamic IP address.

By Greg Yeutter

# Requirements

* Python 2.7 or 3.X

# Set Up

### 1. Git clone this repository into a folder on your computer:

```
cd path_to_desired_location
git clone https://github.com/yeutterg/PublicIpUtility.git
```

### 2. Install the dependencies with PIP:

```
pip install -r requirements.txt
```

Alternatively, a Dockerfile is provided for Docker containers.

### 3. Open Google Sheets and create a new spreadsheet called "Public IP".

 Optionally, you can type "Public IP" in cell A1 and "Updated UTC" in cell B1.

### 4. Follow the instructions [at this link](http://gspread.readthedocs.io/en/latest/oauth2.html) to download a credentials JSON file. 

Rename the downloaded file to "credentials.json" and put it in the same directory as the project.

Be sure to share the Google Sheet with the email provided in the credentials file. Otherwise you will get an error that you cannot access the spreadsheet.

### 5. Run the program to make sure it works:

```
python PublicIP.py
```

### 6. Once you are sure everything works, I recommend running this as a cron job. 

For example, I run the update every 30 minutes. This way, I am never more than 30 minutes out of work from a change of public IP.

Here is an example line in a crontab file:

```
*/30 * * * * python /path_of_project/PublicIP.py
```

