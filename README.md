See the original readme [here](https://github.com/seleniumbase/SeleniumBase).

# Building the image

```bash
docker build --build-arg CHROME_VERSION=132.0.6834.159 -t seleniumbase-executor:132.0.6834.159 .
```

See all possible `CHROME_VERSION` values
[here](https://googlechromelabs.github.io/chrome-for-testing/known-good-versions-with-downloads.json).
