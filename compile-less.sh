#!/bin/bash

compile() {
    lessc "./app/$1/static/$1/less/style.less" "./app/$1/static/$1/css/style.css"
    echo "$1 compiled"
}

compile "auth_custom"
compile "elephant"
compile "friends"
compile "pages"
compile "photos"
compile "posts"
compile "search"
compile "talks"
compile "videos"