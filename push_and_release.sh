#!/bin/bash

TAG=$1

git tag $TAG
git push origin main --tags
gh release create $TAG --title "$TAG" --notes "$TAG"