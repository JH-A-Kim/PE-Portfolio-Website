#!/bin/sh

# *Comments are purely for my own notes
# This script is gonna send a random post request and then search for it using a get request and output the result of if it successfuly sends it or not
# name is just made with a random number
# email is just made with a random number and @email.com
# content is just a static string
name=$RANDOM
email="${RANDOM}@email.com"
content="Testing description"

# we use curl to send request, we define the verb and then the url and then use -F to send form data. (if other type of request we use a different tag)
curl -X POST http://127.0.0.1:5000/api/timeline_post \
-F "name=$name" \
-F "email=$email" \
-F "content=$content"

# using printf instead of echo because printf is more portable and consistent across different shells
printf 'POST Request sent with name: %s, email: %s, content: %s\n' "$name" "$email" "$content"

# now use curl to search for a post in the json body using jq and paramterizing the search with the variables we just created this is just in case any variables have spacing resulting in them being interpreted incorrectly
# .timeline_posts[] is used to get all of the timeline posts as opposed to doing something like timeline_posts[0] to get just index value
# using select to filter the posts based on the values we generated. 
result=$(curl -X GET http://127.0.0.1:5000/api/timeline_post | jq -r --arg N "$name" --arg E "$email" --arg C "$content" '.timeline_posts[] | select(
(.name == ($N)) and
(.email == ($E)) and
(.content == ($C))
)')

# -z will check if the result is empty
# if it is empty then we did not find a matching post because result is empty therefore we print an error message and exit with a non-zero status code
# if it is not empty then we print a sucess message and of course using printf to support better portability between shells.
if [ -z "$result" ]; then
  printf 'Test failed: Matching Post Not Found.' >&2
  exit 1
else
  printf 'Test passed: Matching Post Found.'
fi

