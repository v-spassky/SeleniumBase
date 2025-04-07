See the original readme [here](https://github.com/seleniumbase/SeleniumBase).

# Building the image

```bash
docker build \
    --build-arg CHROME_VERSION=132.0.6834.159 \
    --build-arg GITHUB_PAT=ghp_XtjnedMhXXhB4aHa9jY8T77iVpb3mpL290Y \
    -t seleniumbase-executor:chrome132.0.6834.159 \
    -t seleniumbase-executor:seleniumbase4.35.2 .
```

See all possible `CHROME_VERSION` values
[here](https://googlechromelabs.github.io/chrome-for-testing/known-good-versions-with-downloads.json), see current
SeleniumBase version in [`seleniumbase/__version__.py`](seleniumbase/__version__.py).
