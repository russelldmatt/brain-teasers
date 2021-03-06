#!/bin/bash

if [ "$#" -ne 2 ]; then
    echo "[usage]: $0 <question_name> <difficulty>"
    exit 1
fi

question_name="$1"
difficulty=$2
dir_name=$(echo $question_name | tr '[A-Z]' '[a-z]' | tr ' ' '-')
today=$(date +"%Y-%m-%d")

mkdir $dir_name

touch ${dir_name}/question.md
echo "---
layout: brain-teaser
title:  \"$question_name\"
difficulty: ${difficulty}
add_date: $today
category: brain-teaser
tags:
- question

---
" >> ${dir_name}/question.md

touch ${dir_name}/solution.md
echo "---
layout: solution
title:  \"$question_name\"
category: brain-teaser
tags: solution

---
" >> ${dir_name}/solution.md
