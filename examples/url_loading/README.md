# Example: Using Labelme with URLs

This example demonstrates how to use labelme with image URLs instead of local files.

## Basic Example

Create a file named `image_urls.txt` with one URL per line:

```
https://example.com/images/cat.jpg
https://example.com/images/dog.jpg
https://example.com/images/bird.jpg
```

Then run:

```bash
labelme --url-file image_urls.txt
```

## Using with Pre-signed S3 URLs

If you have images stored in S3, you can generate pre-signed URLs and use them:

```python
# generate_urls.py
import boto3

s3_client = boto3.client('s3')
bucket_name = 'my-bucket'
image_keys = ['images/image1.jpg', 'images/image2.jpg']

with open('s3_urls.txt', 'w') as f:
    for key in image_keys:
        url = s3_client.generate_presigned_url(
            'get_object',
            Params={'Bucket': bucket_name, 'Key': key},
            ExpiresIn=3600  # URL expires in 1 hour
        )
        f.write(url + '\n')
```

Then use the generated file:

```bash
python generate_urls.py
labelme --url-file s3_urls.txt
```

## Important Notes

1. **Label Files**: Annotations are saved as JSON files locally, even when loading images from URLs
2. **Network**: Images are downloaded on-demand, so a stable internet connection is required
3. **Expiration**: If using pre-signed URLs, make sure they don't expire while annotating
4. **Format**: Only direct image URLs are supported (the URL must point to an actual image file)

## Testing

You can test with these public image URLs:

```bash
cat > test_urls.txt << 'EOF'
https://raw.githubusercontent.com/wkentaro/labelme/main/examples/instance_segmentation/data_dataset_voc/JPEGImages/2011_000003.jpg
https://raw.githubusercontent.com/wkentaro/labelme/main/examples/instance_segmentation/data_dataset_voc/JPEGImages/2011_000006.jpg
EOF

labelme --url-file test_urls.txt
```
