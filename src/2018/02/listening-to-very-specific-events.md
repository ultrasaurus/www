---
title: 'listening to very specific events'
date: '2018-02-25T08:05:01-08:00'
status: publish
permalink: /2018/02/listening-to-very-specific-events
author: sarah
excerpt: ''
type: post
id: 6524
category:
    - code
tag: []
post_format: []
---
The model of [declarative eventing](https://www.ultrasaurus.com/2018/02/declarative-eventing/) allows for listening to very specific events and then triggering specific actions. This model simplifies the developer experience, as well as optimizing the system by reducing network traffic.

### AWS S3 bucket trigger

In looking AWS to explain changes in S3 can trigger Lambda functions, I found that the AWS product docs focus on the GUI configuration experience. This probably makes it easy for new folks to write a specific Lambda function; however, it a little harder to see the system patterns before gaining a lot of hands-on experience.

The trigger-action association can be seen more clearly in a [Terraform configuration](https://www.terraform.io/docs/providers/aws/r/s3_bucket_notification.html). Under the hood, Teraform must be using AWS APIs for setting up the trigger). The configuration below specifies that whenever a json file is uploaded to a specific bucket with the path prefix “content-packages” then a specific Lambda function will be executed:

```
resource "aws_s3_bucket_notification" "bucket_terraform_notification" {
    bucket = "${aws_s3_bucket.terraform_bucket.id}"
    lambda_function {
        lambda_function_arn = "${aws_lambda_function.terraform_func.arn}"
        events = ["s3:ObjectCreated:*"]
        filter_prefix = "content-packages/"
        filter_suffix = ".json"
    }
}

```

— via [justinsoliz’ github gist](https://gist.github.com/justinsoliz/8fe711039a76d8261c15f9199c0b29ea)

### Google Cloud events

To illustrate an alternate developer experience, the examples below are shown with **Firebase JavaScript SDK for Google Cloud Functions**, which is idiomatic for JavaScript developers using the [Fluent API style](https://www.martinfowler.com/bliki/FluentInterface.html), popularized by jQuery. The same functionality is available via command line options using `gcloud`, the Google Cloud CLI.

\*\* Cloud Storage trigger\*\*

Below is an example of specifying a trigger for a change to a Google Cloud Storage object in a specific bucket:

```
exports.generateThumbnail = functions.storage.bucket('my-bucket').object().onChange((event) => {
  // ...
});

```

### Cloud Firestore trigger

This approach to filtering events at their source is very powerful when applied to database operations, where a developer can listen to a specific database path, such as with [Cloud Firestore events](https://firebase.google.com/docs/functions/firestore-events):

```
exports.createProduct = functions.firestore
  .document('products/{productId}')
  .onCreate(event => {
    // Get an object representing the document
    // e.g. {'name': 'Wooden Doll', 'description': '...}
    var newValue = event.data.data();

    // access a particular field as you would any JS property
    var name = newValue.name;

    // perform desired operations ...
});

```