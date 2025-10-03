# URL Support in Labelme

This feature allows you to load and annotate images directly from URLs (such as pre-signed S3 URLs) without needing to download them locally first.

## Usage

### Load URLs from a file

Create a text file containing one URL per line:

```
https://example.com/image1.jpg
https://example.com/image2.png
https://s3.amazonaws.com/bucket/image3.jpg?AWSAccessKeyId=...&Signature=...
```

Then run labelme with the `--url-file` argument:

```bash
labelme --url-file urls.txt
```

### Load a single URL

You can also load a single URL directly:

```bash
labelme "https://example.com/image.jpg"
```

## Features

- Supports both HTTP and HTTPS URLs
- Works with pre-signed S3 URLs
- Images are downloaded on-demand when you navigate to them
- No local storage required (images are kept in memory)
- Compatible with all labelme annotation features

## Limitations

- Label files (.json) must still be stored locally
- Network connectivity is required
- Download speed depends on your internet connection
- URLs must point directly to image files (supported formats: JPEG, PNG, etc.)

## Example with Pre-signed S3 URLs

If you have pre-signed S3 URLs, you can use them directly:

```bash
# Create a file with pre-signed URLs
cat > s3_urls.txt << EOF
https://my-bucket.s3.amazonaws.com/image1.jpg?X-Amz-Algorithm=AWS4-HMAC-SHA256&...
https://my-bucket.s3.amazonaws.com/image2.jpg?X-Amz-Algorithm=AWS4-HMAC-SHA256&...
EOF

# Load with labelme
labelme --url-file s3_urls.txt
```

## Notes

- URLs are validated before being added to the file list
- Invalid URLs or URLs that fail to download will be skipped
- The application will display an error message if no valid URLs are found
