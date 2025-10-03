# URL Support Implementation Summary

## Overview
This PR adds support for loading images from URLs (including pre-signed S3 URLs) without needing to download them locally first.

## Changes Made

### Core Implementation

1. **New Utility Module** (`labelme/utils/url.py`)
   - `is_url(path)`: Detects if a path is a URL (http/https)
   - `download_image_from_url(url)`: Downloads image data from a URL

2. **Updated Label File Handler** (`labelme/_label_file.py`)
   - Modified `load_image_file()` to support both local files and URLs
   - Automatically detects URL vs local file path
   - Downloads and processes images from URLs

3. **Enhanced Main Window** (`labelme/app.py`)
   - Added `url_file` parameter to `__init__`
   - New method `importUrlsFromFile()` to load URLs from a text file
   - Updated `loadFile()` to skip file existence check for URLs
   - Automatic filtering of invalid URLs

4. **Command-Line Interface** (`labelme/__main__.py`)
   - Added `--url-file` argument to accept a file containing URLs
   - Properly passes url_file to MainWindow

### Documentation

1. **URL_SUPPORT.md**: Comprehensive guide on URL support features
2. **examples/url_loading/README.md**: Detailed examples including S3 usage
3. **examples/url_loading/sample_urls.txt**: Sample URL file for testing

## Usage

### Basic Usage
```bash
# Create a file with URLs (one per line)
cat > urls.txt << EOF
https://example.com/image1.jpg
https://example.com/image2.jpg
EOF

# Run labelme
labelme --url-file urls.txt
```

### Single URL
```bash
labelme "https://example.com/image.jpg"
```

### Pre-signed S3 URLs
```bash
# URLs can include query parameters (like pre-signed S3 URLs)
cat > s3_urls.txt << EOF
https://bucket.s3.amazonaws.com/image.jpg?AWSAccessKeyId=...&Signature=...
EOF

labelme --url-file s3_urls.txt
```

## Features

✅ Supports HTTP and HTTPS URLs
✅ Works with pre-signed S3 URLs
✅ On-demand image downloading
✅ Automatic URL validation
✅ Backward compatible with local files
✅ No changes to existing functionality

## Testing

All tests pass:
- URL detection and validation
- Image downloading from URLs
- Loading URLs from file
- Loading single URLs directly
- Filtering invalid URLs from file
- Backward compatibility with local files
- Backward compatibility with directory loading

## Technical Details

### URL Detection
Uses `urllib.parse.urlparse()` to detect HTTP/HTTPS schemes

### Image Downloading
- Uses `urllib.request.urlopen()` with 30-second timeout
- Downloads image data into memory
- Processes through PIL for format conversion
- No local file caching required

### Error Handling
- Graceful handling of download failures
- User-friendly error messages
- Invalid URLs automatically filtered out
- Network errors logged appropriately

## Limitations

- Label files (.json) must be stored locally
- Requires active internet connection
- No offline caching
- URLs must point directly to image files
- Pre-signed URLs may expire during annotation sessions

## Backward Compatibility

✅ All existing functionality preserved
✅ Local file loading unchanged
✅ Directory scanning unchanged
✅ No breaking changes
✅ Existing command-line arguments unchanged
