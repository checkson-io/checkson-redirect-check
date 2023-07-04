# Checkson Check for monitoring an HTTP redirect

You can use this check to find out if:

* The original URL presents a valid certificate (for HTTPS)
* The correct status code (`301 - Moved Permanently`) is returned
* The correct `Location` header is returned

It can for example be used if your website has moved to a new domain or if you want to be sure
that an automatic upgrade from HTTP to HTTPS works (see example below).

## Environment variables

| Variable     | Description |
|--------------|-------------|
| URL          | The URL to check |
| REDIRECT_URL | The expected URL to redirect to (contents of the `Location` header) |

## Run check locally

This checks if an HTTPS upgrade works:

```
docker run \
  --env URL=http://instagram.com \
  --env REDIRECT_URL=https://instagram.com/ \
  --rm \
  -it \
  ghcr.io/checkson-io/checkson-redirect-check:main
```
