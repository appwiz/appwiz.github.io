#!/bin/bash

filename=$1

sanitized=${filename// }
sanitized=${sanitized%.html}.html

cp bin/template.html $sanitized
