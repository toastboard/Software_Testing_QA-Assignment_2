if [ "$TRAVIS_PULL_REQUEST" != "false" ] ; then
    curl -u token toastboard:${GITHUB_TOKEN} \
    -d "{\"body\": \"SUCCESS deployed version to staging website shown in deployment message\"}" \
    "https://api.github.com/repos/${TRAVIS_REPO_SLUG}/issues/${TRAVIS_PULL_REQUEST}/comments"
fi