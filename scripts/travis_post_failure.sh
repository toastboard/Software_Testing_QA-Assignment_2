if [ "$TRAVIS_PULL_REQUEST" != "false" ] ; then
    curl -u toastboard${GITHUB_TOKEN} \
    -d "{\"body\": \"FAILURE check Travis CI logs and revise\"}" \
    "https://api.github.com/repos/${TRAVIS_REPO_SLUG}/issues/${TRAVIS_PULL_REQUEST}/comments"
fi