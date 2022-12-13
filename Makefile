


#https://stackoverflow.com/questions/60789862/url-of-the-last-artifact-of-a-github-action-build
all:
#  ntegan@ideapad:~$ curl -s https://api.github.com/repos/ntegan1/opsetspeed/actions/artifacts\?per_page\=1 | jq '[.artifacts[] | {name : .name, archive_download_url : .archive_download_url}]' | jq -r '.[]'
#  {
#    "name": "buildtgz",
#      "archive_download_url": "https://api.github.com/repos/ntegan1/opsetspeed/actions/artifacts/474733089/zip"
#      }
#      ntegan@ideapad:~$ wget 'https://api.github.com/repos/ntegan1/opsetspeed/actions/artifacts/474733089/zip'
#      --2022-12-13 17:41:26--  https://api.github.com/repos/ntegan1/opsetspeed/actions/artifacts/474733089/zip
#      Resolving api.github.com (api.github.com)... 140.82.114.5
#      Connecting to api.github.com (api.github.com)|140.82.114.5|:443... connected.
#      HTTP request sent, awaiting response... 403 Forbidden
#      2022-12-13 17:41:27 ERROR 403: Forbidden.
#
#      ntegan@ideapad:~$ wget 'https://api.github.com/repos/ntegan1/opsetspeed/actions/artifacts/474733089/zip'
#
