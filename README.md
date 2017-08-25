[![Build Status](https://travis-ci.org/pktahinduka/shopeasy-flask-rest-api.svg?branch=master)](https://travis-ci.org/pktahinduka/shopeasy-flask-rest-api)
[![Issue Count](https://codeclimate.com/github/pktahinduka/shopeasy-flask-rest-api/badges/issue_count.svg)](https://codeclimate.com/pktahinduka/shopeasy-flask-rest-api)
[![Coverage Status](https://coveralls.io/repos/github/pktahinduka/shopeasy-flask-rest-api/badge.svg?branch=TravisCI-Test)](https://coveralls.io/github/pktahinduka/shopeasy-flask-rest-api?branch=TravisCI-Test)

# Andela-Bootcamp

ShopEasy: An easy way to create and keep track of items on yur shopping lists.

The challenge of keeping track of shopping items is a need for many individuals that requires an innovative and robust solution that will allow them to remember and share the shopping lists with others

## ShopeasyList API

A flask based API to avail resources for creation of shopeasylists


## SCOPE

|Method | Endpoint | Usage |

|POST| `/api/v1/auth/register` |  Register a user. 
|POST| `/api/v1/auth/login` | Login user.
|POST| `/api/v1/shopeasylists/` | Create a new shopeasy list. 
|GET| `/api/v1/shopeasylists/` | Retrieve all the created shopeasy lists. 
|GET| `/api/v1/shopeasylists/<bucket_id>` | Get a single shopeasy list. 
|PUT| `/api/v1/shopeasylists/<bucket_id>` | Update a single shopeasy list. 
|DELETE| `/api/v1/shopeasylists/<bucket_id>` | Delete single shopeasy list. 
|POST| `/api/v1/shopeasylists/<bucket_id>/items` | Add a new item to this shopeasy list. 
|PUT|`/api/v1/shopeasylists/<bucket_id>/items/<item_id>` | Update this shopeasy list. 
|DELETE|`/api/v1/bucketlists/<bucket_id>/items/<item_id>` | Delete this single shopeasy list. 
|GET| `/api/v1/shopeasylists?per_page=10&page=1` | Pagination to get 10 shopeasy list records.
|GET| `/api/v1/shopeasylists?q=a bucket` | Search for bucket lists with name like a shopeasy. 

## INSTALLATION & SET UP.

1. Clone the project on github: 

2. Checkout into the develop branch using ```git checkout develop```

3. Create a ***virtual environment*** and start the virtual environment

4. Install the dependencies via ```pip install -r requirements.txt```

**Setup Database:**

Install postgres ```brew install postgresql```

1. ```type psql in terminal.```

2. ```On postgres interactive interface, type CREATE DATABASE shopeasylist;```

3. ```source .env```

**Run the Migrations**:
1. ```python manage.py db init```

2. ```python manage.py db migrate```

3. ```python manage.py db upgrade```

4. ```Flask Run```
> The server should be running on [http://127.0.0.1:5000] 

