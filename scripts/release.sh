#!/bin/bash

prev_version=$(poetry version --short)
poetry version $1
version=$(poetry version --short)

sed -i'.save' "s/$prev_version/$version/g" flake8_too_many/checker.py
rm flake8_too_many/checker.py.save

git diff HEAD

printf "The current release version is $version.\n"
printf "Press [y/n] to proceed: "
read yn
case $yn in
    [Yy]* )
        git add --all
        git commit -v
        git tag $version;;
    * ) exit;;
esac
