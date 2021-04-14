---
title: 'firebase auth migration from rails/devise'
date: '2019-02-02T17:53:44-08:00'
status: publish
exported_permalink: /2019/02/firebase-auth-migration-from-rails-and-devise
author: sarah
excerpt: ''
type: post
id: 6730
category:
    - code
tag: []
post_format: []
---
Migration to Firebase from a Heroku-hosted Rails app appears to work seamlessly. I’ve only tested one user, but I could log in with the same password and Facebook account with no end-user intervention.

It took a little experimentation to come up with the correct format for export from `heroku psql` command line:

```
\COPY (select id, email, CASE WHEN confirmed_at IS NULL THEN 'false' ELSE 'true' END as Verified, regexp_replace(encode(encrypted_password::bytea, 'base64'), '\n', '') as hash, password_salt::text, screen_name, '' as photo, '' as google_id, '' as google_email, '' as google_name, '' as google_photo, uid as facebook_id, provider_email as facebook_email, '' as fname, '' as fphoto, '' as twitter_id, '' as twitter_mail, '' as twitter_name, '' as twitter_photo, '' as github_id, '' as github_mail, '' as github_name, '' as github_photo, EXTRACT(EPOCH FROM created_at)::bigint, EXTRACT(EPOCH FROM last_sign_in_at)::bigint, '' as phone FROM speakers ORDER BY id limit 160) TO '~/users.csv' WITH (FORMAT csv, DELIMITER ',');

```

Which I imported with the following command:

```
firebase auth:import ~/users.csv     \
    --hash-algo=BCRYPT               \
    --rounds=10                      \

```

Check your devise config file `config/initializers/devise.rb` — encryption options are configurable there.

Additional Notes
----------------

I found [these samples](https://github.com/firebase/quickstart-js/tree/master/auth) helpful to get a test running *very* quickly.

Firebase auth import requires exactly 26 collumns (for csv import):

```
UID,Email,Email Verified,Password Hash,Password Salt,Name,Photo URL,Google ID,Google Email,Google Display Name,Google Photo URL,Facebook ID,Facebook Email,Facebook Display Name,Facebook Photo URL,Twitter ID,Twitter Email,Twitter Display Name,Twitter Photo URL,GitHub ID,GitHub Email,GitHub Display Name,GitHub Photo URL,User Creation Time,Last Sign-In Time,Phone Number

```