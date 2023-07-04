# Checkson Check for monitoring an HTTP redirect

Use this check on [checkson.io](https://checkson.io) to find out if:

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

## Use check on Checkson

This check can be used on [checkson.io](https://checkson.io) with the following Docker image:

```
ghcr.io/checkson-io/checkson-redirect-check:main
```

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

This checks if a website properly redirects to a new domain
(VictorOps was acquired by Splunk):

```
docker run \
  --env URL=https://victorops.com \
  --env REDIRECT_URL=https://www.splunk.com/en_us/investor-relations/acquisitions/splunk-on-call.html \
  --rm \
  -it \
  ghcr.io/checkson-io/checkson-redirect-check:main
```
