# project One

*In this project I'm trying to integrate some small app into one django project.*

There are currently three app in this project.

* wordcounter - An utility app to count totals number of word and character in paragraph.
* userprofile - handle session related features for the project like

              * signup, login, logout.
              * build profile with profile picture and user details.
              * you can always edit your profile details at any time.

* noteapp - A note-taking app, which you can access after authentication.

          * notes can be access from different device after login.
          * each note is stored with timestamp.
          * you can always delete your notes.

## Run in local host

#### first install project dependency by running

  pip install -r requirements.txt

#### run django development server

  python3 manage.py runserver
